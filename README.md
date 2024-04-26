# Sistema de Gestión de Inventarios

Este es un proyecto de Python que proporciona una interfaz gráfica para gestionar inventarios de productos. Permite agregar, modificar, eliminar y mostrar productos almacenados en una base de datos SQLite.

## Requisitos

- Python 3.x
- Tkinter (incluido en la instalación estándar de Python)
- SQLite (incluido en la instalación estándar de Python)

## Instalación

1. Clona o descarga este repositorio en tu máquina local.
2. Asegúrate de tener Python 3.x instalado en tu sistema.
3. No se requieren pasos de instalación adicionales, ya que el proyecto utiliza bibliotecas estándar de Python.

## Uso

1. Ejecuta el archivo `main.py` para iniciar la aplicación.
2. La aplicación abrirá una ventana con las opciones disponibles.
3. En la pestaña "Agregar Producto", puedes ingresar los detalles del nuevo producto y hacer clic en el botón "Agregar Producto" para agregarlo al inventario.
4. En la pestaña "Modificar Producto", puedes seleccionar un producto existente de la lista desplegable, modificar sus detalles y hacer clic en el botón "Modificar Producto" para guardar los cambios.
5. También puedes eliminar productos desde la pestaña "Modificar Producto" seleccionando un producto y haciendo clic en el botón "Eliminar Producto".
6. El botón "Mostrar Informe" en la ventana principal te permite ver un informe de inventario con detalles de todos los productos almacenados.

## Estructura del Proyecto

- `main.py`: El punto de entrada del programa que inicia la aplicación.
- `bdd.py`: Contiene la clase `BaseDatos` que maneja la conexión y consultas a la base de datos SQLite.
- `inventario.py`: Contiene la clase `Inventario` que maneja la lógica del inventario y las operaciones CRUD.
- `producto.py`: Contiene la definición de la clase `Producto`.
- `interfazinventario.py`: Contiene la clase `InterfazInventario` que define la interfaz de usuario con Tkinter.

## Contribuir

Si quieres contribuir a este proyecto, no dudes en hacerlo


