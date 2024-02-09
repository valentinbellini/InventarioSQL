import tkinter as tk
from interfazinventario import InterfazInventario

# Inicialización de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazInventario(root)
    root.mainloop()