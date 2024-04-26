# Clase Ventas
class Ventas:
    def __init__(self):
        self.ventas = []

    def agregar_venta(self, venta):
        self.ventas.append(venta)

    def eliminar_venta(self, venta):
        self.ventas = [p for p in self.ventas if p.venta_id != venta.venta_id]

    def generar_informe_ventas(self):
        informe = [venta.obtener_venta() for venta in self.ventas]
        return informe