#sales_volume_per_agent
print("----------------------------------------------------")
print("Sales_volume_per_agent")
def sales_volume_per_agent(orders):
    sales_volume = {}
    
    i = 0
    
    while i < len(orders):
        sales_agent_id = orders[i][1]  # Få sælgerens ID
        order_value = orders[i][2]      # Få ordrebeløbet
        
        # Opdater salgsvolumen for sælgeren
        if sales_agent_id in sales_volume:
            sales_volume[sales_agent_id] += order_value
        else:
            sales_volume[sales_agent_id] = order_value
        
        i += 1
    
    # Konverter ordbogen til en liste af lister, divider med 100 for at få kroner
    result = []
    for agent, volume in sales_volume.items():
        result.append([agent, volume / 100])
    return result

orders = [
    ['dk-34922423', 'pja', 55_960_00],
    ['dk-34927049', 'pja', 35_905_31],
    ['dk-34929950', 'ssk', 1_000_000_00],
    ['dk-34929950', 'pja', 72_048_67],
]

result = sales_volume_per_agent(orders)

# Udskriv resultatet
for row in result:
    print(f"Sælger ID: {row[0]}, Salgsvolumen: {row[1]:,.2f}")

# #Opgave 2
# print("----------------------------------------------------")
# print("Opgave 2")
# def order_value(orderLine):
#     result = {}

#     i = 0
#     while i < len(orderLine):
#         orderId = orderLine[i][0]



# orders_line = [['dk-34922423',     1, 55_000_00,  5_000_00, 'DKK', 'ds-35-8'],
#  ['dk-34927049',     7,  5_129_33,         0, 'DKK', 'f6-427-b'],
#  ['dk-34922423', 1_000,      5_96,         0, 'DKK', 'ds-102-0'],
#  ['se-440958',       3, 70_430_00, 11_290_00, 'SEK', 'ds-35-8'],
#  ['se-440958',      50,     30_08,         0, 'SEK', 'f6-514-c'],
#  ['se-440055',     178,      7_03,         0, 'SEK', 'ds-102-0'],
# ]

# order_value(orders_line)