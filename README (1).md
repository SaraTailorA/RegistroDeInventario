# Inventory Management System

¡Bienvenido a mi proyecto de gestión de inventarios! Este es un programa desarrollado en **Python** diseñado para facilitar el registro, control, análisis estadístico y almacenamiento persistente del inventario de una empresa.

---

## Descripción
Este sistema permite interactuar con un menú dinámico para gestionar un conjunto de productos. El programa garantiza la integridad de los datos mediante validaciones, ofrece un resumen financiero y estadístico avanzado, y permite guardar y cargar la información en archivos CSV, asegurando que los datos no se pierdan al cerrar la aplicación.

---

## Tecnologías y Conceptos Utilizados

Para el desarrollo de esta herramienta, apliqué conceptos fundamentales de programación que aseguran un código limpio y funcional:

### **Tecnologías**
* **Lenguaje:** Python 3.x
* **Almacenamiento:** .csv (Comma-Separated Values)
* **Entorno de ejecución:** Terminal / Consola
* **Editor:** VS Code (Visual Studio Code)

### **Conceptos de Programación Aplicados**
* **Estructuras de Datos:** Uso de `listas` para el almacenamiento global y `diccionarios` para representar cada producto (nombre, precio, cantidad).
* **Control de Flujo:** Implementación de ciclos `while` para la persistencia del menú y condicionales `if-elif-else` para la lógica de navegación.
* **Validación de Datos (Error Handling):** Uso de bloques `try-except` para prevenir cierres inesperados si el usuario ingresa datos no numéricos.
* **Modularización:** Organización del código mediante `funciones` específicas (`add_product`, `show_inventory`, `calculate_statistics`) para mejorar la legibilidad.
* **Lógica Aritmética:** Cálculos automatizados para obtener subtotales y estadísticas globales del inventario.
* **Operaciones CRUD Completas:** Lógica para Crear, Leer, Actualizar y Borrar (Create, Read, Update, Delete) registros del inventario.
* **Persistencia de Datos (File I/O):** Lectura y escritura de archivos de texto usando gestores de contexto `(with open())` para un manejo seguro de la memoria.
* **Modularización Avanzada:** Arquitectura dividida en múltiples archivos (`week2.py, library.py, files.py`) e importación de módulos para separar la interfaz, la lógica de negocio y el acceso a datos.
* **Buenas Prácticas:** Implementación de Docstrings para la documentación interna de funciones y algoritmos de fusión (`Merge/Overwrite`) para evitar duplicidad de datos.

---

## Cómo funciona

1.  **Registro con Validación:** Permite añadir productos asegurando que el precio sea decimal y la cantidad sea un entero.
2.  **Visualización de Inventario:** Listado organizado de todos los productos registrados.
3.  **Cálculo de Estadísticas:** Genera automáticamente el valor total monetario del stock y el conteo de unidades físicas, además calcula automáticamente el valor total monetario del stock, el conteo de unidades físicas, identifica el producto más caro y el producto con mayor inventario.
4.  **Interfaz Intuitiva:** Menú interactivo que guía al usuario durante toda la ejecución.
5.  **Gestión de Productos (CRUD):** 
 * Añadir: Registra productos asegurando que precio y cantidad sean números positivos. 
 * Buscar / Actualizar / Eliminar: Encuentra productos específicos por nombre para modificar sus valores o retirarlos del sistema.
6.  **Persistencia en CSV:**
 * Guardar: Exporta el inventario actual a un archivo .csv.
 * Cargar: Importa datos desde un archivo, omitiendo filas corruptas y preguntando al usuario si desea Sobrescribir el inventario actual o Fusionarlo (sumando el stock de productos existentes).
 * Visualización: Listado organizado en consola de todos los productos registrados.

---
## Estado del Proyecto

> El programa ha evolucionado de un script básico a una aplicación de consola modular y persistente. Demuestra un dominio sólido de las estructuras de datos en Python, el control de flujo, la validación estricta de errores y la manipulación segura de archivos del sistema.
