from library import *
from files import *

# Lista principal para almacenar los productos (Inventario en memoria)
inventory = []

# Variable para controlar el bucle del menú
option = ""

# Bucle principal para mostrar el menú hasta que el usuario elija salir (9)
while option != "9":
    print("=" * 40)
    print("                   MENU                  ")
    print("=" * 40)
    print("1. Add product")
    print("2. Show inventory")
    print("3. Calculate statistics")
    print("4. Search product")
    print("5. Update product")
    print("6. Delete product")
    print("7. Save CSV")
    print("8. Load CSV")
    print("9. Exit")

    option = input("\nChoose an option: ")

    if option == "1":
        add_product(inventory)

    elif option == "2":
        show_inventory(inventory)

    elif option == "3":
        calculate_statistics(inventory)

    elif option == "4":
        search_product(inventory)

    elif option == "5":
        update_product(inventory)

    elif option == "6":
        delete_product(inventory)

    elif option == "7":
        file_name = input("Enter file name to save (example: data.csv): ")
        save_csv(inventory, file_name)

    elif option == "8":
        file_name = input("Enter file name to load: ")
        loaded_inventory = load_csv(file_name)
        
        # Si se cargó información correctamente, preguntamos qué hacer con ella
        if loaded_inventory:
            choice = input("Overwrite current inventory? (Y/N): ").strip().upper()
            
            if choice == "Y":
                # Sobrescribir: reemplazamos la lista actual
                inventory = loaded_inventory
                print("Inventory overwritten successfully.\n")
            else:
                # Fusionar por nombre (si existe, suma cantidad y actualiza precio)
                for new_item in loaded_inventory:
                    found = False
                    for existing_item in inventory:
                        if existing_item["name"].lower() == new_item["name"].lower():
                            existing_item["quantity"] += new_item["quantity"]
                            existing_item["price"] = new_item["price"]
                            found = True
                            break
                    
                    # Si no se encontró el producto, lo agregamos como nuevo
                    if not found:
                        inventory.append(new_item)
                print("Inventory merged successfully.\n")

    elif option == "9":
        print("Closing program... Goodbye!")

    else:
        print("Invalid option. Please enter a number from 1 to 9.\n")

# Este programa gestiona un inventario completo utilizando módulos (archivos separados).
# Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar),
# calcular estadísticas avanzadas y mantener la persistencia de datos mediante archivos CSV.