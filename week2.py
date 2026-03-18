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
