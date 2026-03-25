# Pregunta por el nombre del producto.
product_name = input("Enter the product name: ")

# Pregunta por el precio y validarlo.
while True:
    try:
        price = float(input("Enter the product price: "))
        break
    except:
        print("Invalid value. You must enter a number for the price.")

# Pregunta por la cantidad y validarlo.
while True:
    try:
        quantity = int(input("Enter the product quantity: "))
        break
    except:
        print("Invalid value. You must enter an integer for the quantity.")

# Calcula el costo total.
total_cost = price * quantity

# Mostrar los resultados en la consola

print("\n" + "*" * 50)
print("        Product Information ")
print("*" * 50 + "\n")
print("Product name:",     product_name)
print("Unit price $:",            price)
print("Quantity:",             quantity)
print("Total cost $:",       total_cost)

# Este programa pregunta por el nombre del producto, su precio y la cantidad.
# Valida que el precio sea un decimal y la cantidad un entero.
# Sí el usuario ingresa un valor inválido, el programa pide por los datos de nuevo.
# Después de recibir los valores correcto, calcula el costo total multiplicando
# el precio por la cantidad y finalmente muestra los resultados en la consola.

from library import *

# Lista para almacenar los productos
inventory = []

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
        add_product(inventory)

    elif option == "2":
        show_inventory(inventory)

    elif option == "3":
        calculate_statistics(inventory)

    elif option == "4":
        print("Closing program...")

    else:
        print("Invalid option. Try again.\n")