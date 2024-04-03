import json

def find_lowest_costing_lego_set(json_data):
    # Load the JSON data
    data = json.loads(json_data)

    # Initialize a variable to store the lowest price
    lowest_price = float('inf')

    # Iterate through each store's sales data
    for store in data:
        for sale in store['sales']:
            # Check if the set is a small size
            if sale['size'] == 'small':
                # Update the lowest price if the current price is lower
                lowest_price = min(lowest_price, sale['price'])

    # Return the lowest price as a double
    return lowest_price

# Example usage:
json_data = """
[
{
"date": "2023-07-01",
"store": "LEGO Store 1",
"sales": [
{
"type": "Star Wars",
"size": "small",
"units": 100,
"price": 14.99
},
{
"type": "Star Wars",
"size": "medium",
"units": 80,
"price": 19.99
},
{
"type": "Star Wars",
"size": "large",
"units": 60,
"price": 24.99
},
# ... (more sales data)
]
# ... (more store data)
}
]
"""

result = find_lowest_costing_lego_set(json_data)
print(result)