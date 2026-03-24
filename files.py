def save_csv(inventory, file_name):
    """
    Guarda el inventario actual en un archivo CSV.
    Utiliza 'with open' para un manejo seguro de archivos.
    """
    if len(inventory) == 0:
        print("Inventory is empty, nothing to save.\n")
        return

    try:
        # 'with' abre el archivo y lo cierra automáticamente al terminar
        with open(file_name, "w", encoding="utf-8") as file:
            # Escribir encabezado
            file.write("name,price,quantity\n")

            # Escribir productos
            for product in inventory:
                line = f"{product['name']},{product['price']},{product['quantity']}\n"
                file.write(line)

        print(f"Inventory saved successfully in {file_name}.\n")

    except Exception as e:
        # Atrapa cualquier error de permisos o de escritura sin cerrar la app
        print(f"Error saving file: {e}\n")


def load_csv(file_name):
    """
    Carga productos desde un archivo CSV.
    Omite filas inválidas y cuenta cuántas fueron para avisarle al usuario.
    """
    loaded_inventory = []
    skipped_lines = 0

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

            # Si el archivo está vacío
            if len(lines) <= 1:
                print("File is empty or only has headers.\n")
                return loaded_inventory

            # Recorrer a partir de la fila 1 para saltar el encabezado
            for i in range(1, len(lines)):
                parts = lines[i].strip().split(",")

                # Validar que tenga exactamente 3 columnas
                if len(parts) != 3:
                    skipped_lines += 1
                    continue

                try:
                    name = parts[0].strip()
                    price = float(parts[1])
                    quantity = int(parts[2])

                    # Validar que no sean negativos
                    if price < 0 or quantity < 0:
                        skipped_lines += 1
                        continue

                    product = {
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    }
                    loaded_inventory.append(product)

                except ValueError:
                    # Si el precio o la cantidad no son números, se omite esta fila
                    skipped_lines += 1

        print(f"\nFile loaded. {len(loaded_inventory)} products found.")
        
        if skipped_lines > 0:
            print(f"Warning: {skipped_lines} invalid rows were skipped.")
            
        return loaded_inventory

    except FileNotFoundError:
        print("\nError: The specified file was not found.\n")
        return None
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}\n")
        return None
