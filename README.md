# Inventory Management System

¡Bienvenido a mi proyecto de gestión de inventarios! Este es un programa desarrollado en **Python** diseñado para facilitar el registro, control y análisis estadístico de inventario de una empresa.

---

## Descripción
Este sistema permite interactuar con un menú dinámico para gestionar un conjunto de productos. El programa garantiza la integridad de los datos mediante validaciones y ofrece un resumen financiero del inventario total.

---

## Tecnologías y Conceptos Utilizados

Para el desarrollo de esta herramienta, apliqué conceptos fundamentales de programación que aseguran un código limpio y funcional:

### **Tecnologías**
* **Lenguaje:** Python 3.x
* **Entorno de ejecución:** Terminal / Consola
* **Editor:** VS Code (Visual Studio Code)

### **Conceptos de Programación Aplicados**
* **Estructuras de Datos:** Uso de `listas` para el almacenamiento global y `diccionarios` para representar cada producto (nombre, precio, cantidad).
* **Control de Flujo:** Implementación de ciclos `while` para la persistencia del menú y condicionales `if-elif-else` para la lógica de navegación.
* **Validación de Datos (Error Handling):** Uso de bloques `try-except` para prevenir cierres inesperados si el usuario ingresa datos no numéricos.
* **Modularización:** Organización del código mediante `funciones` específicas (`add_product`, `show_inventory`, `calculate_statistics`) para mejorar la legibilidad.
* **Lógica Aritmética:** Cálculos automatizados para obtener subtotales y estadísticas globales del inventario.

---

## Cómo funciona

1.  **Registro con Validación:** Permite añadir productos asegurando que el precio sea decimal y la cantidad sea un entero.
2.  **Visualización de Inventario:** Listado organizado de todos los productos registrados.
3.  **Cálculo de Estadísticas:** Genera automáticamente el valor total monetario del stock y el conteo de unidades físicas.
4.  **Interfaz Intuitiva:** Menú interactivo que guía al usuario durante toda la ejecución.

---
## Estado del Proyecto

> El programa se encuentra actualmente como un proyecto de aprendizaje básico, demostrando el manejo de entradas, la validación de datos, listas, diccionarios y modulaciones en Python.
