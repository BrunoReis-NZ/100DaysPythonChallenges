# Project 2: Product Inventory System (Advanced)
# Scenario: You are developing an inventory system for a store. The inventory is stored as a nested dictionary with categories as keys. Each category contains another dictionary where the keys are product names and the values are their stock and price.
#
# Requirements:
# Define the System:
# # Create an inventory dictionary where each key is a category,
# and the value is another dictionary containing product names as keys and their stock and price as values.
#
# Add New Product:
# # Write a function add_product(inventory, category, product, stock, price) that adds a new product to a category.
#
# Update Product Details:
# # Write a function update_product(inventory, category, product, key, value) that updates a specific detail of a product.
#
# Retrieve Product Details:
# # Write a function get_product(inventory, category, product) that prints all details of a product.
#
# Display All Products:
# # Write a function display_inventory(inventory) to print all categories and their products with details.

print("Project 2: Product Inventory System (Advanced)\n")

def add_product(inventory, category, product, stock, price):
    if category not in inventory:
        inventory[category] = {}
    inventory[category][product] = {"stock": stock, "price": price}

def update_product(inventory, category, product, key, value):
    if category in inventory and product in inventory[category]:
        inventory[category][product][key] = value
    else:
        print(f"Product {product} in category {category} not found.")

def get_product(inventory, category, product):
    if category in inventory and product in inventory[category]:
        print(inventory[category][product])
    else:
        print(f"Product {product} in category {category} not found.")

def display_inventory(inventory):
    for category, products in inventory.items():
        print(f"Category: {category}")
        for product, details in products.items():
            print(f"  {product}: Stock = {details['stock']}, Price = {details['price']}")

# Inventory dictionary
inventory = {}

# Add products
add_product(inventory, "Electronics", "Laptop", 10, 999.99)
add_product(inventory, "Electronics", "Smartphone", 20, 699.99)
add_product(inventory, "Clothing", "T-shirt", 50, 19.99)

# Update product details
update_product(inventory, "Electronics", "Laptop", "stock", 8)

# Get product details
get_product(inventory, "Electronics", "Laptop")

# Display inventory
display_inventory(inventory)
