import tkinter as tk
from tkinter import ttk, messagebox 

# Importación de clases
from bdd import BaseDatos  
from inventario import Inventario 
from producto import Producto  

# Interfaz de Usuario con Tkinter
class InterfazInventario:
    def __init__(self, root):
        # Inicialización de la clase BaseDatos para manejar la base de datos
        self.base_datos = BaseDatos()
        # Inicialización de la clase Inventario para manejar el inventario de productos
        self.inventario = Inventario()
        # Carga de los productos desde la base de datos al inventario
        self.cargar_productos_desde_db()

        # Configuración de la ventana principal de la aplicación
        self.root = root
        self.root.title("Sistema de Gestión de Inventarios")
        self.root.geometry("500x400")

        # Configuración del notebook para mostrar pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        # Creación de las pestañas "Agregar Producto" y "Modificar Producto"
        self.pagina_agregar = ttk.Frame(self.notebook)
        self.pagina_modificar = ttk.Frame(self.notebook)
        self.notebook.add(self.pagina_agregar, text='Agregar Producto')
        self.notebook.add(self.pagina_modificar, text='Modificar Producto')

        # Creación de la interfaz para agregar un nuevo producto
        self.crear_interfaz_agregar_producto()
        # Creación de la interfaz para modificar un producto existente
        self.crear_interfaz_modificar_producto()
        # Creación del botón para mostrar el informe de inventarios
        self.crear_boton_mostrar_informe()

    # Método para cargar los productos desde la base de datos al inventario
    def cargar_productos_desde_db(self):
        productos_db = self.base_datos.obtener_productos()
        self.inventario.productos = productos_db

    # Método para crear la interfaz para agregar un nuevo producto
    def crear_interfaz_agregar_producto(self):
        etiquetas_agregar = ["Nombre del Producto", "Descripción", "Precio", "Stock", "Proveedor"]
        self.entries_agregar = {}  # Diccionario para almacenar las entradas de datos

        # Creación de etiquetas y entradas para cada campo del producto
        for i, etiqueta in enumerate(etiquetas_agregar):
            tk.Label(self.pagina_agregar, text=etiqueta, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.pagina_agregar, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries_agregar[etiqueta] = entry

        # Botón para agregar el producto
        self.boton_agregar = tk.Button(self.pagina_agregar, text="Agregar Producto", command=self.agregar_producto, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.boton_agregar.grid(row=len(etiquetas_agregar) + 1, column=0, columnspan=2, pady=10)

    # Método para crear la interfaz para modificar un producto existente
    def crear_interfaz_modificar_producto(self):
        etiquetas_modificar = ["Seleccione Producto:", "Nombre del Producto", "Descripción", "Precio", "Stock", "Proveedor"]

        # Combobox para seleccionar el producto a modificar
        self.combo_modificar = ttk.Combobox(self.pagina_modificar, values=["Seleccionar"] + [producto.nombre for producto in self.inventario.productos],
                                            font=("Arial", 12))
        self.combo_modificar.grid(row=0, column=1, padx=10, pady=5)
        self.combo_modificar.set("Seleccionar")
        # Asociar la función para actualizar las entradas al seleccionar un producto
        self.combo_modificar.bind("<<ComboboxSelected>>", self.actualizar_datos_producto_seleccionado)

        self.entries_modificar = {}  # Diccionario para almacenar las entradas de datos

        # Creación de etiquetas y entradas para el nuevo precio y stock del producto
        for i, etiqueta in enumerate(etiquetas_modificar[1:]):
            tk.Label(self.pagina_modificar, text=etiqueta, font=("Arial", 12)).grid(row=i + 1, column=0, padx=10, pady=5)
            entry = tk.Entry(self.pagina_modificar, font=("Arial", 12))
            entry.grid(row=i + 1, column=1, padx=10, pady=5)
            self.entries_modificar[etiqueta] = entry

        # Botón para modificar el producto
        self.boton_modificar = tk.Button(self.pagina_modificar, text="Modificar Producto", command=self.modificar_producto, font=("Arial", 12), bg="#008CBA", fg="white")
        self.boton_modificar.grid(row=len(etiquetas_modificar) + 1, column=0, columnspan=2, pady=10)

    # Método para crear el botón para mostrar el informe de inventarios
    def crear_boton_mostrar_informe(self):
        self.boton_mostrar_informe = tk.Button(self.root, text="Mostrar Informe", command=self.mostrar_informe, font=("Arial", 12), bg="#333", fg="white")
        self.boton_mostrar_informe.pack(pady=10)

    # Método para agregar un nuevo producto al inventario y a la base de datos
    def agregar_producto(self):
        try:
            # Obtención de los datos del nuevo producto desde las entradas de datos
            nombre = self.entries_agregar["Nombre del Producto"].get()
            descripcion = self.entries_agregar["Descripción"].get()
            precio = float(self.entries_agregar["Precio"].get())
            stock = int(self.entries_agregar["Stock"].get())
            proveedor = self.entries_agregar["Proveedor"].get()

            # Creación del objeto Producto con los datos obtenidos
            producto = Producto(len(self.inventario.productos) + 1, nombre, descripcion, precio, stock, proveedor)
            # Agregado del producto al inventario
            self.inventario.agregar_producto(producto)
            # Agregado del producto a la base de datos
            self.base_datos.agregar_producto(producto)
            # Actualización de las opciones en el combobox de modificar producto
            self.combo_modificar["values"] = ["Seleccionar"] + [p.nombre for p in self.inventario.productos]
            messagebox.showinfo("Éxito", "Producto agregado correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese datos válidos para el producto.")

    # Método para modificar un producto existente en el inventario y en la base de datos
    def modificar_producto(self):
        selected_product = self.combo_modificar.get()
        if selected_product != "Seleccionar":
            # Obtención del objeto Producto seleccionado para modificar
            producto = next((p for p in self.inventario.productos if p.nombre == selected_product), None)
            if producto:
                nuevo_precio = self.entries_modificar["Precio"].get()
                nuevo_stock = self.entries_modificar["Stock"].get()
                nuevo_proveedor = self.entries_modificar["Proveedor"].get()
                nueva_descripcion = self.entries_modificar["Descripción"].get()

                if nuevo_precio and nuevo_stock and nuevo_proveedor and nueva_descripcion:
                    try:
                        nuevo_precio = float(nuevo_precio)
                        nuevo_stock = int(nuevo_stock)

                        # Actualización del precio, stock, proveedor y descripción del producto
                        producto.actualizar_precio(nuevo_precio)
                        producto.actualizar_stock(nuevo_stock)
                        producto.actualizar_proveedor(nuevo_proveedor)
                        producto.actualizar_descripcion(nueva_descripcion)

                        # Cierre y reestablecimiento de la conexión con la base de datos
                        self.base_datos.cerrar_conexion()
                        self.base_datos = BaseDatos()
                        messagebox.showinfo("Éxito", "Producto modificado correctamente.")
                    except ValueError:
                        messagebox.showerror("Error", "Ingrese datos válidos para precio y stock.")
                else:
                    messagebox.showerror("Error", "Ingrese nuevo precio, stock, proveedor y descripción.")
            else:
                messagebox.showerror("Error", "Producto no encontrado.")

    # Método para actualizar las entradas con los datos del producto seleccionado
    def actualizar_datos_producto_seleccionado(self, event):
        selected_product = self.combo_modificar.get()
        if selected_product != "Seleccionar":
            producto = next((p for p in self.inventario.productos if p.nombre == selected_product), None)
            if producto:
                # Mostrar los datos del producto en las entradas correspondientes
                self.entries_modificar["Nombre del Producto"].delete(0, tk.END)
                self.entries_modificar["Nombre del Producto"].insert(0, producto.nombre)
                self.entries_modificar["Descripción"].delete(0, tk.END)
                self.entries_modificar["Descripción"].insert(0, producto.descripcion)
                self.entries_modificar["Precio"].delete(0, tk.END)
                self.entries_modificar["Precio"].insert(0, str(producto.precio))
                self.entries_modificar["Stock"].delete(0, tk.END)
                self.entries_modificar["Stock"].insert(0, str(producto.cantidad_stock))
                self.entries_modificar["Proveedor"].delete(0, tk.END)
                self.entries_modificar["Proveedor"].insert(0, producto.proveedor)

    # Método para mostrar el informe de inventarios
    def mostrar_informe(self):
        informe = self.inventario.generar_informe()
        mensaje = "\n\n".join(informe)
        messagebox.showinfo("Informe de Inventarios", mensaje)

