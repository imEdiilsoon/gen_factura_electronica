import os
import random

opcion = -1

while opcion != 2:
  print("\nElige una opción: \n\n | 1 - Crear una nueva Factura. \n | 2 - Salir del programa. \n")
  opcion = int(input())
  
  if opcion == 2:
    os.system("cls")
    exit

  productos = []
  precios = []
  cantidades = []

  if opcion == 1:
    os.system("cls")
    opcion_menu_factura = -1
    id_factura = random.randint(1000, 9000)

    print("\n Ingrese el nombre del cliente: \n")
    cliente = input("")

    while opcion_menu_factura != 2:

      print("\n Ingrese el nombre del producto: \n")
      productos.append(input(""))
      print("\n Ingrese el valor unitario del producto: $\n")
      precios.append(int(input()))
      print("\n Ingrese la cantidad del producto: \n")
      cantidades.append(int(input()))

      os.system("cls")
      print("\nElige una opción: \n\n | 1 - Registrar otro producto. \n | 2 - Imprimir factura. \n")
      opcion_menu_factura = int(input())

      if(opcion_menu_factura == 2):
        os.system("cls")
        print("__________________________________________________________")
        print(f"\n|  🧾 Factura Generada N°: {id_factura}\n")
        
        for i in range(len(productos)):
          print(f"✅ Producto: {productos[i]} | Precio Unit: {precios[i]} | Cantidad: {cantidades[i]}")

        valor_neto = 0
        for i in range(len(precios)):
          valor_neto = valor_neto + precios[i]

        iva = valor_neto * 0.19
        total = iva + valor_neto


        print(f"\nValor Neto: $ {valor_neto}")
        print(f"IVA: $ {iva}")
        print(f"Total: $ {total}")

        print(f"\n|  Cliente: {cliente}. !Gracias por elegirnos! ❤️\n")
        print("__________________________________________________________")
