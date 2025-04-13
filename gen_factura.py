import os
import random
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

opcion = -1

while opcion != 2:
  print("\nElige una opción: \n\n | 1 - Crear una nueva Factura. \n | 2 - Salir del programa. \n")
  opcion = int(input("→ "))
  
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

    print("| 👤 Información básica del cliente.")
    print("\nIngrese el nombre del cliente:")
    cliente = input("→ ")
    print("\nIngrese la cedula del cliente:")
    cedula = int(input("→ "))
    print("\nIngrese el correo del cliente:")
    correo = input("→ ")

    while opcion_menu_factura != 2:

      os.system("cls")
      print("| 🛒 Información del producto.")
      print("\n Ingrese el nombre del producto:")
      productos.append(input("→ "))
      print("\n Ingrese el valor unitario del producto:")
      precios.append(int(input("$ ")))
      print("\n Ingrese la cantidad del producto:")
      cantidades.append(int(input("→ ")))

      os.system("cls")
      print("\nElige una opción: \n\n | 1 - Registrar otro producto. \n | 2 - Imprimir factura. \n")
      opcion_menu_factura = int(input("→ "))

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
        total = int(iva + valor_neto)

        fecha = datetime.now().strftime('%d/%m/%Y | %H:%M:%S')

        print(f"\nValor Neto: $ {valor_neto}")
        print(f"IVA: $ {iva}")
        print(f"Total: $ {total}")

        print("\n|  👤 Información del cliente:\n")
        print(f"Nombre: {cliente}.")
        print(f"Cedula: {cedula}.")
        print(f"Correo: {correo}.")
        print("\nGracias por tu compra! ❤️\n")
        print(f"|  📅 Fecha: {fecha}")
        print("__________________________________________________________")

        opcion_pdf_gen = -1
        print("\n¿Desea guardar esta factura en un PDF?\n\n | 1 - Si.\n | 2 - No.\n")
        opcion_pdf_gen = int(input("→ "))

        if opcion_pdf_gen == 1:
          def Generar_factura(nombre_archivo):
            ruta_guardar_pdf= "pdf_generados"
            ruta_completa = os.path.join(ruta_guardar_pdf, nombre_archivo)

            c = canvas.Canvas(ruta_completa, pagesize=letter)
            
            text = c.beginText()
            text.setTextOrigin(50, 750)
            text.setFont("Courier", 12)

            text.textLine(f"Factura n°: {id_factura}")
            text.textLine(" ")
            text.textLine(" ")
            text.textLine("Información de la compra:")
            text.textLine(" ")

            for i in range(len(productos)):
              suma_precio = precios[i] * cantidades[i]
              text.textLine(f"{productos[i]} x ({cantidades[i]})      $ {suma_precio}")

            text.textLine(" ")
            text.textLine(f"Valor Neto: {valor_neto}")
            text.textLine(f"IVA: {iva}")
            text.textLine(f"Total: {total}")
            text.textLine(" ")
            text.textLine(" ")

            text.textLine("Información del cliente:")
            text.textLine(" ")
            text.textLine(f"Nombre: {cliente}")
            text.textLine(f"Cedula: {cedula}")
            text.textLine(f"Correo: {correo}")
            text.textLine(" ")
            text.textLine("¡Gracias por tu compra!")
            text.textLine(" ")
            text.textLine(f"Factura generada el: {fecha}")
            
            c.drawText(text)
            c.showPage()
            c.save()
            print(f"\nLa Factura n°: {id_factura}. Se guardó correctamente.")

          Generar_factura(f"{id_factura}.pdf")
        elif opcion_pdf_gen == 2:
          os.system("cls")
