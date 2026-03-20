# Función para agregar un producto
def add_product(inventory):
    # Solicitar nombre del producto
    name = input("Enter product name: \n")

    # Validación precio y cantidad
    try:
        price = float(input("Enter product price $: \n"))
        quantity = int(input("Enter product quantity: \n"))
        # Crear diccionario del producto
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        # Agregar producto a la lista
        inventory.append(product)

        print("\nProduct added successfully.\n")
    except:
        print("\nError: Invalid input. Please enter correct values.\n")
        return  # Sale de la función si hay error
    



# Función para mostrar el inventario
def show_inventory(inventory):
    # Verificar si el inventario está vacío
    if len(inventory) == 0:
        print("\nInventory is empty.\n")
    else:
        print("-" * 40 )
        print(" Inventory ")
        print("-" * 40 + "\n")
        # Recorrer lista con for
        for product in inventory:
            print("Product:", product["name"],
                  "| Price:", product["price"],
                  "| Quantity:", product["quantity"])
        print()

# Función para calcular estadísticas
def calculate_statistics(inventory):
    total_value = 0
    total_quantity = 0

    # Recorrer inventario
    for product in inventory:
        total_value += product["price"] * product["quantity"]
        total_quantity += product["quantity"]
    print("\n"+"*" * 40)
    print("     Statistics     ")
    print("*" * 40 + "\n")
    print("Total inventory value:",         total_value)
    print("Total quantity of products:", total_quantity)
    print()