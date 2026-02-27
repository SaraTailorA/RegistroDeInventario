print("###############################################################")
print("#             RiwiTechStore - Registro De Ventas              #")
print("###############################################################")


register_more_sales = True


while register_more_sales == True:
     print("\n----------------------- NUEVA VENTA ---------------------------")

     client_name = input("Ingrese aqui el nombre del cliente: ")
     unit_price = float(input("Ingrese aqui el precio unitario del producto ($): "))
     quantity = int(input("Ingrese aquí la cantidad: "))
     vip = input("El cliente tiene membresia VIP (si/no): ").strip().lower() == "si"

     subtotal = unit_price * quantity

     if vip:
        discount = subtotal * 0.10
     else:
        discount = 0.0

     total = subtotal - discount

     print("---------------------------------------------------------------")
     print("|               RESUMEN DE LA TRANSACCION                     |")
     print("---------------------------------------------------------------")

     print(f"Client:                                        {client_name}  ")
     print(f"Subtotal:                                      ${subtotal:.2f}")
     print(f"Descuento Aplicado:                            ${discount:.2f}")
     print(f"Total final a pagar:                           ${total:.2f}   ")

     print("--------------------------------------------------------------")
     print("               ¡Venta registrada exitosamente!                ")

     print("                    ¡Gracias por su compra!                   ")



     register_more_sales = input("¿Desea registrar otra venta? (si/no): ").strip().lower() == "si"
     


    