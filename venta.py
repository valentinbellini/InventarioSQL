from producto import Producto  # Importamos la clase Producto del módulo producto.py


# Clase Venta
class Venta:
    def __init__(self, venta_id, cant_articulos, medio_pago, total, productos):
        self.venta_id = venta_id
        self._cant_articulos = cant_articulos
        self._medio_pago = medio_pago
        self._total = total
        self._productos = productos

    # CANTIDAD ARTICULOS
    @property
    def cant_articulos(self):
        return self._cant_articulos
    @cant_articulos.setter
    def cant_articulos(self, nueva_cant_articulos):
        self._cant_articulos = nueva_cant_articulos

    # MEDIO DE PAGO
    @property
    def medio_pago(self):
        return self._medio_pago
    @medio_pago.setter
    def medio_pago(self, nuevo_medio_pago):
        self._medio_pago = nuevo_medio_pago
    
    # TOTAL  
    @property
    def total(self):
        return self._total
    @total.setter
    def total(self, nuevo_total):
        self._total = nuevo_total
    
    # PRODUCTOS
    @property
    def productos(self):
        return self._productos
    @productos.setter
    def productos(self, nuevos_productos):
        self._productos = nuevos_productos

    # OBTENER VENTA
    def obtener_venta(self):
        venta = f"ID: {self.venta_id}\nCantidad de artículos: {self.cant_articulos}\nMedio de pago: {self.medio_pago}\n"
        venta += f"Total: {self.total}\nProductos: {self.productos}"
        return venta