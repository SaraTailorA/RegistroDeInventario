def add_product(inventory):
    """
    Agrega un nuevo producto al inventario validando que el precio y cantidad
    sean números positivos.
    """
    name = input("Enter product name: \n").strip()

    try:
        price = float(input("Enter product price $: \n"))
        quantity = int(input("Enter product quantity: \n"))

        if price < 0:
            print("Price cannot be negative.\n")
            return

        if quantity < 0:
            print("Quantity cannot be negative.\n")
            return

        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        inventory.append(product)
        print("\nProduct added successfully.\n")

    # Usamos ValueError para atrapar solo errores de conversión a int/float
    except:
        print("\nError: Invalid input. You must enter numbers for price and quantity.\n")


def show_inventory(inventory):
    """Muestra todos los productos actuales en formato de tabla simple."""
    if len(inventory) == 0:
        print("\nInventory is empty.\n")
    else:
        print("-" * 50)
        print("                  Inventory ")
        print("-" * 50)
        for product in inventory:
            print(f"Product: {product['name']} | Price: ${product['price']} | Quantity: {product['quantity']}")
        print()


def calculate_statistics(inventory):
    """Calcula y muestra el valor total, cantidades y productos destacados."""
    if len(inventory) == 0:
        print("\nInventory is empty. No statistics to show.\n")
        return

    total_value = 0
    total_quantity = 0
    
    # Variables para producto más caro y mayor stock
    most_expensive_name = ""
    highest_price = -1
    highest_stock_name = ""
    highest_stock = -1

    for product in inventory:
        total_value += product["price"] * product["quantity"]
        total_quantity += product["quantity"]
        
        # Lógica para encontrar el más caro
        if product["price"] > highest_price:
            highest_price = product["price"]
            most_expensive_name = product["name"]
            
        # Lógica para encontrar el de mayor stock
        if product["quantity"] > highest_stock:
            highest_stock = product["quantity"]
            highest_stock_name = product["name"]

    print("\n" + "*" * 50)
    print("                   Statistics     ")
    print("*" * 50)
    print(f"Total inventory value:       ${total_value}")
    print(f"Total quantity of products:  {total_quantity}")
    print(f"Most expensive product:      {most_expensive_name} (${highest_price})")
    print(f"Product with highest stock:  {highest_stock_name} ({highest_stock} units)")
    print()


def search_product(inventory):
    """Busca un producto por su nombre e imprime sus detalles."""
    name = input("Enter product name to search: ").strip()

    for product in inventory:
        if product["name"].lower() == name.lower():
            print(f"\nProduct found -> Name: {product['name']} | Price: ${product['price']} | Quantity: {product['quantity']}\n")
            return

    print("Product not found.\n")


def update_product(inventory):
    """Actualiza el precio y cantidad de un producto existente."""
    name = input("Enter product name to update: ").strip()

    for product in inventory:
        if product["name"].lower() == name.lower():
            try:
                new_price = float(input("New price $: "))
                new_quantity = int(input("New quantity: "))

                if new_price < 0 or new_quantity < 0:
                    print("Values cannot be negative.\n")
                    return

                product["price"] = new_price
                product["quantity"] = new_quantity
                print("Product updated successfully.\n")
                return
            except:
                print("Error: Invalid values. Please enter numbers.\n")
                return

    print("Product not found.\n")


def delete_product(inventory):
    """Elimina un producto del inventario mediante su nombre."""
    name = input("Enter product name to delete: ").strip()

    for product in inventory:
        if product["name"].lower() == name.lower():
            inventory.remove(product)
            print("Product deleted successfully.\n")
            return

    print("Product not found.\n")