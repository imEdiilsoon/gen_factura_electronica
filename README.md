# 🧾 Generador de Facturas | v1

Este proyecto implementa un algoritmo en Python que permite generar facturas de manera automatizada a partir de la información proporcionada por el usuario. El sistema contempla los siguientes elementos clave:

### ✅ Características actuales:

- Información del cliente (Nombre, Cedula de Ciudadania o DNI, Teléfono de contacto.).
- Lista de productos adquiridos.
- Cantidad de unidades por producto.
- Precio unitario de cada producto.
- Cálculo del valor neto de la factura.
- Aplicación del IVA correspondiente.
- Generación del total final a pagar.
- Generación y guardado de la factura en formato PDF.

El resultado es una factura clara, detallada y lista para ser entregada al cliente


### 🖼️ Vista previa

# Factura generada en la consola del equipo:
![facutra-consola.png](https://i.postimg.cc/wjZn6fkD/facutra-consola.png)

# Factura generada en archivo PDF:
![factura-pdf.png](https://i.postimg.cc/rw0YYGLs/factura-pdf.png)

---

## 📦 Módulos utilizados

Este proyecto requiere tener instalado [Python](https://www.python.org/) para su ejecución.

### 🔧 Librerías estándar:

- `os`:  
  Utilizado para ejecutar comandos del sistema, como limpiar la consola.

- `random`:  
  Utilizado para generar un identificador único aleatorio (ID) para cada factura, con un valor entre 1000 y 9000.

- `datetime`:  
  Utilizado para obtener la fecha actual con el fin de ser mostrada en la factura electrónica.

- `reportlab`:  
  Utilizado para la generación de archivos PDF.

---

## 📈 Próximas implementaciones

- [x] Añadir la fecha y hora de emisión de la factura. ¡Completado! 🎉
- [x] Exportar la factura a un archivo PDF. ¡Completado! 🎉
- [ ] Almacenar los productos en una lista y al seleccionarlos traer el precio asociado al producto.
- [ ] Incluir información adicional del cliente (correo, dirección, etc.).
- [ ] Registro y selección de clientes guardados para facturación rápida.
- [ ] Almacenar la factura en una base de datos para control interno.
- [ ] Implementar una interfaz gráfica para ingresar los datos del cliente y los productos de forma visual e intuitiva.

---

## 🧩 Conclusión

Este generador de facturas es una herramienta funcional y en constante evolución, ideal para automatizar procesos básicos de facturación. A medida que se integren nuevas funcionalidades, su utilidad aumentará tanto para pequeños negocios como para proyectos personales o académicos.  
¡Tu colaboración o feedback es bienvenido para seguir mejorando esta solución!

---