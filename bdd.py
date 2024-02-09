import sqlite3
from tkinter import ttk, messagebox 
from producto import Producto  # Importamos la clase Producto del módulo producto.py

# Clase para manejar la base de datos
class BaseDatos:
    def __init__(self):
        # Conexión a la base de datos SQLite
        self.conexion = sqlite3.connect("inventario.db")
        self.cursor = self.conexion.cursor()  # Creación de un cursor para ejecutar consultas SQL
        self.crear_tabla()  # Llamada al método para crear la tabla si no existe

    def crear_tabla(self):
        # Ejecución de la consulta SQL para crear la tabla de productos si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                producto_id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                precio REAL NOT NULL,
                cantidad_stock INTEGER NOT NULL,
                proveedor TEXT
            )
        ''')
        self.conexion.commit()  # Confirmación de los cambios en la base de datos

    def obtener_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()  # Obtención de todas las filas resultantes
        return [Producto(*row) for row in rows] # Creación de objetos Producto a partir de las filas y retorno de una lista de productos

    def agregar_producto(self, producto):
        # Ejecución de la consulta SQL para insertar un nuevo producto en la tabla
        self.cursor.execute('''
            INSERT INTO productos (nombre, descripcion, precio, cantidad_stock, proveedor)
            VALUES (?, ?, ?, ?, ?)
        ''', (producto.nombre, producto.descripcion, producto.precio, producto.cantidad_stock, producto.proveedor))
        self.conexion.commit()  # Confirmación de los cambios en la base de datos

    def eliminar_producto(self, producto):
        self.cursor.execute('''
             DELETE FROM productos WHERE producto_id=?               
        ''', (producto.producto_id,))
        self.conexion.commit()
        
    def actualizar_producto(self, producto):
        try:
            # Ejecutar la consulta SQL para actualizar el producto
            self.cursor.execute('''
                UPDATE productos SET nombre=?, descripcion=?, precio=?, cantidad_stock=?, proveedor=? WHERE producto_id=?
            ''', (producto.nombre, producto.descripcion, producto.precio, producto.cantidad_stock, producto.proveedor, producto.producto_id))
            self.conexion.commit()  # Confirmar los cambios en la base de datos
        except sqlite3.Error as error:
            # Manejar cualquier error de base de datos
            messagebox.showerror("Error en base de datos", f"No se pudo actualizar el producto: {error}")
    
    def cerrar_conexion(self):
        self.conexion.close()  # Cierre de la conexión a la base de datos
