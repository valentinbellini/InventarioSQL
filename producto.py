# Clase Producto
class Producto:
    def __init__(self, producto_id, nombre, descripcion, precio, cantidad_stock, proveedor):
        self.producto_id = producto_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad_stock = cantidad_stock
        self.proveedor = proveedor

    def actualizar_stock(self, nuevo_stock):
        self.cantidad_stock = nuevo_stock

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        
    def actualizar_proveedor(self, nuevo_proveedor):
        self.proveedor = nuevo_proveedor
    
    def actualizar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def obtener_detalles(self):
        detalles = f"ID: {self.producto_id}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\n"
        detalles += f"Precio: {self.precio}\nStock: {self.cantidad_stock}\nProveedor: {self.proveedor}"
        return detalles