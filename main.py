import tkinter as tk
from funciones import accion_boton

def main():
    ventana = tk.Tk()
    ventana.title("App de Prueba")

    boton = tk.Button(ventana, text="Botón de prueba", command=accion_boton)
    boton.pack(padx=50, pady=30)

    ventana.mainloop()

if __name__ == "__main__":
    main()
