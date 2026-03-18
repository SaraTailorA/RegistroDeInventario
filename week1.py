# Ask for the product name
product_name = input("Enter the product name: ")

# Ask for and validate the price
while True:
    try:
        price = float(input("Enter the product price: "))
        break
    except ValueError:
        print("Invalid value. You must enter a number for the price.")

# Ask for and validate the quantity
while True:
    try:
        quantity = int(input("Enter the product quantity: "))
        break
    except ValueError:
        print("Invalid value. You must enter an integer for the quantity.")

# Calculate the total cost
total_cost = price * quantity

# Display results in the console
print("\n--- Product Information ---")
print("Product name:", product_name)
print("Unit price:", price)
print("Quantity:", quantity)
print("Total cost:", total_cost)

# This program asks the user for the name of a product, its price, and the quantity.
# It validates that the price is a decimal number and that the quantity is an integer.
# If the user enters an invalid value, the program asks for the data again.
# After receiving correct values, it calculates the total cost by multiplying
# the price by the quantity and finally displays all the product information in the console.