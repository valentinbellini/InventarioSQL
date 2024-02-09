import tkinter as tk
from tkinter import ttk, messagebox #, simpledialog

from bdd import BaseDatos
from inventario import Inventario
from producto import Producto

# Interfaz de Usuario con Tkinter
class InterfazInventario:
    def __init__(self, root):
        self.base_datos = BaseDatos()
        self.inventario = Inventario()
        self.cargar_productos_desde_db()

        self.root = root
        self.root.title("Sistema de Gestión de Inventarios")
        self.root.geometry("500x400")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        self.pagina_agregar = ttk.Frame(self.notebook)
        self.pagina_modificar = ttk.Frame(self.notebook)

        self.notebook.add(self.pagina_agregar, text='Agregar Producto')
        self.notebook.add(self.pagina_modificar, text='Modificar Producto')

        self.crear_interfaz_agregar_producto()
        self.crear_interfaz_modificar_producto()
        self.crear_boton_mostrar_informe()

    def cargar_productos_desde_db(self):
        productos_db = self.base_datos.obtener_productos()
        self.inventario.productos = productos_db

    def crear_interfaz_agregar_producto(self):
        etiquetas_agregar = ["Nombre del Producto", "Descripción", "Precio", "Stock", "Proveedor"]
        self.entries_agregar = {}

        for i, etiqueta in enumerate(etiquetas_agregar):
            tk.Label(self.pagina_agregar, text=etiqueta, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.pagina_agregar, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries_agregar[etiqueta] = entry

        self.boton_agregar = tk.Button(self.pagina_agregar, text="Agregar Producto", command=self.agregar_producto, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.boton_agregar.grid(row=len(etiquetas_agregar) + 1, column=0, columnspan=2, pady=10)

    def crear_interfaz_modificar_producto(self):
        etiquetas_modificar = ["Seleccione Producto:", "Nuevo Precio", "Nuevo Stock"]
        self.combo_modificar = ttk.Combobox(self.pagina_modificar, values=["Seleccionar"] + [producto.nombre for producto in self.inventario.productos],
                                            font=("Arial", 12))
        self.combo_modificar.grid(row=0, column=1, padx=10, pady=5)
        self.combo_modificar.set("Seleccionar")

        self.entries_modificar = {}

        for i, etiqueta in enumerate(etiquetas_modificar[1:]):
            tk.Label(self.pagina_modificar, text=etiqueta, font=("Arial", 12)).grid(row=i + 1, column=0, padx=10, pady=5)
            entry = tk.Entry(self.pagina_modificar, font=("Arial", 12))
            entry.grid(row=i + 1, column=1, padx=10, pady=5)
            self.entries_modificar[etiqueta] = entry

        self.boton_modificar = tk.Button(self.pagina_modificar, text="Modificar Producto", command=self.modificar_producto, font=("Arial", 12), bg="#008CBA", fg="white")
        self.boton_modificar.grid(row=len(etiquetas_modificar) + 1, column=0, columnspan=2, pady=10)

    def crear_boton_mostrar_informe(self):
        self.boton_mostrar_informe = tk.Button(self.root, text="Mostrar Informe", command=self.mostrar_informe, font=("Arial", 12), bg="#333", fg="white")
        self.boton_mostrar_informe.pack(pady=10)

    def agregar_producto(self):
        try:
            nombre = self.entries_agregar["Nombre del Producto"].get()
            descripcion = self.entries_agregar["Descripción"].get()
            precio = float(self.entries_agregar["Precio"].get())
            stock = int(self.entries_agregar["Stock"].get())
            proveedor = self.entries_agregar["Proveedor"].get()

            producto = Producto(len(self.inventario.productos) + 1, nombre, descripcion, precio, stock, proveedor)
            self.inventario.agregar_producto(producto)
            self.base_datos.agregar_producto(producto)
            self.combo_modificar["values"] = ["Seleccionar"] + [p.nombre for p in self.inventario.productos]
            messagebox.showinfo("Éxito", "Producto agregado correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese datos válidos para el producto.")

    def modificar_producto(self):
        selected_product = self.combo_modificar.get()
        if selected_product != "Seleccionar":
            producto = next((p for p in self.inventario.productos if p.nombre == selected_product), None)
            if producto:
                nuevo_precio = self.entries_modificar["Nuevo Precio"].get()
                nuevo_stock = self.entries_modificar["Nuevo Stock"].get()

                if nuevo_precio and nuevo_stock:
                    try:
                        nuevo_precio = float(nuevo_precio)
                        nuevo_stock = int(nuevo_stock)

                        producto.actualizar_precio(nuevo_precio)
                        producto.actualizar_stock(nuevo_stock)

                        self.base_datos.cerrar_conexion()
                        self.base_datos = BaseDatos()
                        messagebox.showinfo("Éxito", "Producto modificado correctamente.")
                    except ValueError:
                        messagebox.showerror("Error", "Ingrese datos válidos para precio y stock.")
                else:
                    messagebox.showerror("Error", "Ingrese nuevo precio y stock.")
            else:
                messagebox.showerror("Error", "Producto no encontrado.")

    def mostrar_informe(self):
        informe = self.inventario.generar_informe()
        mensaje = "\n\n".join(informe)
        messagebox.showinfo("Informe de Inventarios", mensaje)