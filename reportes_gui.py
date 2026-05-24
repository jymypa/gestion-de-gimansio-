import tkinter as tk
import sqlite3


def conectar():
    return sqlite3.connect("gimnasio.db")


def mostrar_reportes():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM socios")
    total_socios = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM entrenadores")
    total_entrenadores = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM pagos")
    total_pagos = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(monto) FROM pagos")
    ingresos = cursor.fetchone()[0]

    conexion.close()

    if ingresos is None:
        ingresos = 0

    resultado.config(
        text=f"""
REPORTE GENERAL

Total de socios: {total_socios}
Total de entrenadores: {total_entrenadores}
Total de pagos: {total_pagos}
Ingresos acumulados: Bs. {ingresos}
"""
    )


def abrir_ventana_reportes():

    global resultado

    ventana = tk.Toplevel()

    ventana.title("Reportes")
    ventana.geometry("420x300")
    ventana.resizable(False, False)

    tk.Label(
        ventana,
        text="REPORTES DEL SISTEMA",
        font=("Arial", 14, "bold")
    ).pack(pady=20)

    tk.Button(
        ventana,
        text="Mostrar Reporte",
        width=20,
        command=mostrar_reportes
    ).pack(pady=10)

    resultado = tk.Label(
        ventana,
        text="",
        font=("Arial", 11, "bold"),
        justify="left"
    )

    resultado.pack(pady=10)