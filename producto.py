# Clase Producto
class Producto:
    def __init__(self, producto_id, nombre, descripcion, precio, cantidad_stock, proveedor):
        self.producto_id = producto_id
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._cantidad_stock = cantidad_stock
        self._proveedor = proveedor

    # NOMBRE
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # DESCRIPCION
    @property
    def descripcion(self):
        return self._descripcion
    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self._descripcion = nueva_descripcion
    
    # PRECIO  
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, nuevo_precio):
        self._precio = nuevo_precio
    
    # STOCK
    @property
    def cantidad_stock(self):
        return self._cantidad_stock
    @cantidad_stock.setter
    def cantidad_stock(self, nuevo_stock):
        self._cantidad_stock = nuevo_stock

    # PROVEEDOR
    @property
    def proveedor(self):
        return self._proveedor
    @proveedor.setter
    def proveedor(self, nuevo_proveedor):
        self._proveedor = nuevo_proveedor

    # OBTENER DETALLES
    def obtener_detalles(self):
        detalles = f"ID: {self.producto_id}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\n"
        detalles += f"Precio: {self.precio}\nStock: {self.cantidad_stock}\nProveedor: {self.proveedor}"
        return detalles