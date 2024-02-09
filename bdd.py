import sqlite3
from producto import Producto

# Clase para manejar la base de datos
class BaseDatos:
    def __init__(self):
        self.conexion = sqlite3.connect("inventario.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
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
        self.conexion.commit()

    def obtener_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()
        return [Producto(*row) for row in rows]

    def agregar_producto(self, producto):
        self.cursor.execute('''
            INSERT INTO productos (nombre, descripcion, precio, cantidad_stock, proveedor)
            VALUES (?, ?, ?, ?, ?)
        ''', (producto.nombre, producto.descripcion, producto.precio, producto.cantidad_stock, producto.proveedor))
        self.conexion.commit()

    def cerrar_conexion(self):
        self.conexion.close()
