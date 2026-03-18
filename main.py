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

# Lista para almacenar los productos del inventario
inventory = []

# Función para agregar un producto
def add_product():
    # Solicitar nombre del producto
    name = input("Enter product name: ")

    # Validación simple de precio y cantidad
    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
    except ValueError:
        print("Error: Invalid input. Please enter correct values.\n")
        return  # Sale de la función si hay error

    # Crear diccionario del producto
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    # Agregar producto a la lista
    inventory.append(product)

    print("Product added successfully.\n")


# Función para mostrar el inventario
def show_inventory():
    # Verificar si el inventario está vacío
    if len(inventory) == 0:
        print("Inventory is empty.\n")
    else:
        print("\n--- Inventory ---")
        # Recorrer lista con for
        for product in inventory:
            print("Product:", product["name"],
                  "| Price:", product["price"],
                  "| Quantity:", product["quantity"])
        print()


# Función para calcular estadísticas
def calculate_statistics():
    total_value = 0
    total_quantity = 0

    # Recorrer inventario
    for product in inventory:
        total_value += product["price"] * product["quantity"]
        total_quantity += product["quantity"]

    print("\n--- Statistics ---")
    print("Total inventory value:", total_value)
    print("Total quantity of products:", total_quantity)
    print()


# Variable para controlar el menú
option = ""

# Bucle principal (SIN while True)
while option != "4":
    print("=== MENU ===")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Calculate statistics")
    print("4. Exit")

    option = input("Choose an option: ")

    # Condicionales
    if option == "1":
        add_product()

    elif option == "2":
        show_inventory()

    elif option == "3":
        calculate_statistics()

    elif option == "4":
        print("Exiting program...")

    else:
        print("Invalid option. Try again.\n")


# Comentario final
# Este programa permite gestionar un inventario básico.
# El usuario puede agregar productos, ver el inventario
# y calcular estadísticas como el valor total y cantidad de productos.