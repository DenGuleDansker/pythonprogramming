from kafka import KafkaAdminClient, KafkaProducer, KafkaConsumer, TopicPartition
from kafka.admin import NewTopic
from collections import namedtuple
import json
import sys
from datetime import datetime

KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']

class Kafka:
    def __init__(self, topic, partition_count=1, ):
        self.topic = topic
        self.partition_count = partition_count
        self._admin_client = None
        self._producer = None
        self._consumer = None
    
    def send(self, key, value):
        producer = self._get_producer()
        with FallibleOperation(f'Sending Kafka message to topic "{self.topic}" with key {key}'):
            producer.send(self.topic, key=key, value=value).get()

    def start_interactive_producer_loop(self):
        item_name = self.topic[:-1]
        while True:
            print()
            item_id = input(f'Enter {item_name} ID (leave empty to quit): ').strip()
            if not item_id:
                break
            while True:
                item_details = input(f'Enter {item_name} details as JSON: ').strip() or "null"
                try:
                    item_details_json = json.loads(item_details)
                except:
                    print('Invalid JSON. Please redo.')
                    continue
                self.send(item_id, item_details_json)
                break

    def seek(self, partition, offset):
        consumer = self._get_consumer()
        tp = TopicPartition(self.topic, partition)
        with FallibleOperation(f'Seeking to offset {offset} on partition {partition} of topic "{self.topic}"', fatal=True):
            consumer.assign([tp])
            consumer.seek(tp, offset)

    def __iter__(self):
        consumer = self._get_consumer()
        if not consumer.assignment():
            consumer.subscribe([self.topic])
        for message in consumer:
            yield Message(
                message.partition,
                message.offset,
                datetime.fromtimestamp(message.timestamp / 1000.0).isoformat(timespec='milliseconds'),
                message.key.decode(),
                json.loads(message.value.decode()) if message.value else None
            )
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self._admin_client:
            with FallibleOperation(f'Closing admin client for topic "{self.topic}"'):
                self._admin_client.close()
        if self._consumer:
            with FallibleOperation(f'Closing consumer of topic "{self.topic}"'):
                self._consumer.close()
        if self._producer:
            with FallibleOperation(f'Closing producer of topic "{self.topic}"'):
                self._producer.close()
        return False

    def _get_producer(self):
        if not self._producer:
            self._create_topic_if_needed()
            with FallibleOperation(f'Creating Kafka producer of topic "{self.topic}"', fatal=True):
                self._producer = KafkaProducer(
                    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                    key_serializer=lambda k: k.encode(),
                    value_serializer=lambda v: None if v is None else json.dumps(v).encode(),
                    max_block_ms=1000,
                )
        return self._producer

    def _create_topic_if_needed(self):
        if not self._check_topic_exists():
            self._create_topic()

    def _check_topic_exists(self):
        if self.topic in self._list_topics():
            print(f'Required topic "{self.topic}" confirmed.')
            return True
        else:
            print(f'Required topic "{self.topic}" does not exist.')
            return False

    def _list_topics(self):
        admin_client = self._get_admin_client()
        with FallibleOperation(f'Retrieving available Kafka topics', fatal=True):
            return admin_client.list_topics()

    def _create_topic(self):
        admin_client = self._get_admin_client()
        with FallibleOperation(f'Creating topic "{self.topic}"', fatal=True):
            admin_client.create_topics(new_topics=[NewTopic(
                name=self.topic,
                num_partitions=self.partition_count,
                replication_factor=1,
                topic_configs={'cleanup.policy': 'compact', 'retention.ms': '-1'})])

    def _get_admin_client(self):
        if not self._admin_client:
            with FallibleOperation(f'Connecting to Kafka as admin client "{self.topic}"', fatal=True):
                self._admin_client = KafkaAdminClient(
                    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                    client_id=self.topic,
                )
        return self._admin_client

    def _get_consumer(self):
        if not self._consumer:
            self._require_topic()
            with FallibleOperation(f'Creating Kafka consumer of topic "{self.topic}"', fatal=True):
                self._consumer = KafkaConsumer(
                    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                    enable_auto_commit=False,
                    auto_offset_reset='earliest',
                )
        return self._consumer

    def _require_topic(self):
        if not self._check_topic_exists():
            sys.exit(1)

class FallibleOperation:
    def __init__(self, message, fatal=False):
        self.message = message
        self.fatal = fatal
    
    def __enter__(self):
        print(self.message, end='...\n')
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(self.message + ' [FAILED]')
            print(exc_value)
            if self.fatal:
                sys.exit(1)
        return True

Message = namedtuple('Message', ['partition', 'offset', 'timestamp', 'key', 'value'])