#sales_volume_per_agent
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
    return [[agent, volume / 100] for agent, volume in sales_volume.items()]

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