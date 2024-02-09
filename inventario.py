# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos = [p for p in self.productos if p.producto_id != producto.producto_id]


    def buscar_producto(self, producto_id):
        for producto in self.productos:
            if producto.producto_id == producto_id:
                return producto
        return None

    def generar_informe(self):
        informe = [producto.obtener_detalles() for producto in self.productos]
        return informe