from database import crear_base_datos
import tkinter as tk
from tkinter import messagebox

from entrenadores_gui import abrir_ventana_entrenadores
from pagos_gui import abrir_ventana_pagos
from reportes_gui import abrir_ventana_reportes
from socios_gui import abrir_ventana_socios
def abrir_socios():
    abrir_ventana_socios()


def abrir_entrenadores():
    abrir_ventana_entrenadores()


def abrir_pagos():
    abrir_ventana_pagos()


def abrir_reportes():
    abrir_ventana_reportes()

def salir():
    if messagebox.askyesno("Salir", "¿Seguro que deseas salir?"):
        ventana.destroy()


crear_base_datos()

ventana = tk.Tk()
ventana.title("Sistema de Gestión de Gimnasio")
ventana.geometry("500x450")
ventana.resizable(False, False)
titulo = tk.Label(
    ventana,
    text="SISTEMA DE GESTIÓN DE GIMNASIO",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=30)

tk.Button(ventana, text="Gestión de Clientes", width=25, height=2, command=abrir_socios).pack(pady=10)
tk.Button(ventana, text="Gestión de Entrenadores", width=25, height=2, command=abrir_entrenadores).pack(pady=10)
tk.Button(ventana, text="Gestión de Pagos", width=25, height=2, command=abrir_pagos).pack(pady=10)
tk.Button(ventana, text="Reportes", width=25, height=2, command=abrir_reportes).pack(pady=10)
tk.Button(ventana, text="Salir", width=25, height=2, command=salir).pack(pady=20)

ventana.mainloop()