from library import add_product, show_inventory, calculate_statistics

# Variable para controlar el menú
option = ""

# Bucle principal (SIN while True)
while option != "4":
    print("=" *40 )
    print("                   MENU                  ")
    print("=" *40 +"\n")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Calculate statistics")
    print("4. Exit")

    option = input("\nChoose an option: ")

    # Condicionales
    if option == "1":
        add_product()

    elif option == "2":
        show_inventory()

    elif option == "3":
        calculate_statistics()

    elif option == "4":
        print("Closing program...")

    else:
        print("Invalid option. Try again.\n")


# Este programa permite gestionar un inventario básico.
# El usuario puede agregar productos, ver el inventario
# y calcular estadísticas como el valor total y cantidad de productos.
