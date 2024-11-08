# Small Project: Shopping Cart Calculator
# Goal: Create a small program that asks the user for item prices and quantities, calculates totals, and formats the output.
#
# Instructions:
#
# Ask the user to input the price of an item and the quantity of that item.
# Use type conversion to ensure they’re treated as floats and integers respectively.
# Calculate the total for each item (price * quantity).
# Calculate the grand total of all items.
# Display each item's total and the grand total formatted as currency.
# Use number manipulation and string formatting to display everything in a user-friendly way.


print("Shopping Cart Calculator\n")

#Get item1 details
item1_description = input("Enter 'item1' description: ")
item1_price = float(input("Enter the 'item1' price: "))
item1_quantity = int(input("Enter the 'item1 quantity': "))
item1_total = item1_price * item1_quantity

#Get item2 details
item2_description = input("Enter 'item2' description: ")
item2_price = float(input("Enter the 'item2' price: "))
item2_quantity = int(input("Enter the 'item2 quantity': "))
item2_total = item2_price * item2_quantity

#Get item3 details
item3_description = input("Enter 'item3' description: ")
item3_price = float(input("Enter the 'item3' price: "))
item3_quantity = int(input("Enter the 'item3 quantity': "))
item3_total = item3_price * item3_quantity

#Grand total
grand_total = item1_total + item2_total + item3_total

print(f"Your cart contains:\n "
      f"\t{item1_quantity} {item1_description} totalizing ${item1_total:,.2f}\n"
      f"\t{item2_quantity} {item2_description} totalizing ${item2_total:,.2f}\n"
      f"\t{item3_quantity} {item3_description} totalizing ${item3_total:,.2f}\n"
      f"The total amount of your cart is: ${grand_total:,.2f}.")



