import tkinter as tk
import sqlite3
from datetime import datetime, timedelta


def conectar():
    return sqlite3.connect("gimnasio.db")


# ---------------- FUNCIONES ----------------

def guardar_pago():

    fecha_pago = datetime.now()

    fecha_vencimiento = fecha_pago + timedelta(days=30)

    pago = fecha_pago.strftime("%d/%m/%Y")

    vencimiento = fecha_vencimiento.strftime("%d/%m/%Y")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id
        FROM socios
        WHERE ci = ?
    """, (entry_ci.get(),))

    socio = cursor.fetchone()

    if socio:

        socio_id = socio[0]

        cursor.execute("""
            INSERT INTO pagos (
                socio_id,
                monto,
                fecha_pago,
                fecha_vencimiento
            )
            VALUES (?, ?, ?, ?)
        """, (
            socio_id,
            entry_monto.get(),
            pago,
            vencimiento
        ))

        conexion.commit()

        resultado.config(
            text=f"""
PAGO REGISTRADO

CI: {entry_ci.get()}
Monto: Bs. {entry_monto.get()}
Fecha Pago: {pago}
Vence: {vencimiento}
"""
        )

    else:

        resultado.config(
            text="Socio no encontrado"
        )

    conexion.close()


def buscar_pago():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT pagos.id,
               socios.nombre,
               socios.apellido,
               pagos.monto,
               pagos.fecha_pago,
               pagos.fecha_vencimiento
        FROM pagos
        INNER JOIN socios
        ON pagos.socio_id = socios.id
        WHERE socios.ci = ?
    """, (entry_ci.get(),))

    pago = cursor.fetchone()

    conexion.close()

    if pago:

        resultado.config(
            text=f"""
PAGO ENCONTRADO

Socio: {pago[1]} {pago[2]}
Monto: Bs. {pago[3]}
Fecha Pago: {pago[4]}
Vence: {pago[5]}
"""
        )

    else:

        resultado.config(
            text="Pago no encontrado"
        )


def mostrar_pagos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT socios.nombre,
               socios.apellido,
               pagos.monto,
               pagos.fecha_pago,
               pagos.fecha_vencimiento
        FROM pagos
        INNER JOIN socios
        ON pagos.socio_id = socios.id
    """)

    pagos = cursor.fetchall()

    conexion.close()

    texto = "LISTA DE PAGOS\n\n"

    for pago in pagos:

        texto += f"""
Socio: {pago[0]} {pago[1]}
Monto: Bs. {pago[2]}
Fecha Pago: {pago[3]}
Vence: {pago[4]}

"""

    resultado.config(text=texto)


def eliminar_pago():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM pagos
        WHERE id = (
            SELECT pagos.id
            FROM pagos
            INNER JOIN socios
            ON pagos.socio_id = socios.id
            WHERE socios.ci = ?
        )
    """, (entry_ci.get(),))

    conexion.commit()
    conexion.close()

    limpiar()

    resultado.config(
        text="Pago eliminado"
    )


def limpiar():

    entry_ci.delete(0, tk.END)
    entry_monto.delete(0, tk.END)

    resultado.config(text="")


# ---------------- VENTANA ----------------

def abrir_ventana_pagos():

    global entry_ci
    global entry_monto
    global resultado

    ventana = tk.Toplevel()

    ventana.title("Gestión de Pagos")
    ventana.geometry("550x550")
    ventana.resizable(False, False)

    tk.Label(
        ventana,
        text="CI del Socio"
    ).grid(row=0, column=0, pady=5)

    tk.Label(
        ventana,
        text="Monto"
    ).grid(row=1, column=0, pady=5)

    entry_ci = tk.Entry(ventana, width=30)
    entry_monto = tk.Entry(ventana, width=30)

    entry_ci.grid(row=0, column=1)
    entry_monto.grid(row=1, column=1)

    tk.Button(
        ventana,
        text="Registrar Pago",
        width=18,
        command=guardar_pago
    ).grid(row=2, column=0, pady=10)

    tk.Button(
        ventana,
        text="Buscar Pago",
        width=18,
        command=buscar_pago
    ).grid(row=2, column=1)

    tk.Button(
        ventana,
        text="Eliminar Pago",
        width=18,
        command=eliminar_pago
    ).grid(row=3, column=0)

    tk.Button(
        ventana,
        text="Mostrar Pagos",
        width=18,
        command=mostrar_pagos
    ).grid(row=3, column=1)

    tk.Button(
        ventana,
        text="Limpiar",
        width=18,
        command=limpiar
    ).grid(row=4, column=0, columnspan=2, pady=10)

    resultado = tk.Label(
        ventana,
        text="",
        font=("Arial", 10, "bold"),
        justify="left"
    )

    resultado.grid(
        row=5,
        column=0,
        columnspan=2,
        pady=15
    )