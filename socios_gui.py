import tkinter as tk
import sqlite3
from datetime import datetime


def conectar():
    return sqlite3.connect("gimnasio.db")


# ---------------- FUNCIONES ----------------

def guardar():

    if entry_ci.get() == "":

        resultado.config(
            text="Ingrese el número de carnet",
            fg="red"
        )

        return

    fecha_actual = datetime.now()

    fecha_inscripcion = fecha_actual.strftime("%d/%m/%Y")

    conexion = conectar()
    cursor = conexion.cursor()

    try:

        cursor.execute("""
            INSERT INTO socios (
                nombre,
                apellido,
                ci,
                telefono,
                fecha_inscripcion,
                estado
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            entry_nombre.get(),
            entry_apellido.get(),
            entry_ci.get(),
            entry_telefono.get(),
            fecha_inscripcion,
            "Activo"
        ))

        conexion.commit()

        label_registro.config(
            text=f"Registrado: {fecha_inscripcion}"
        )

        resultado.config(
            text="Socio guardado correctamente",
            fg="green"
        )

    except sqlite3.IntegrityError:

        resultado.config(
            text="El CI ya existe",
            fg="red"
        )

    conexion.close()


def buscar():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM socios
        WHERE ci = ?
    """, (entry_ci.get(),))

    socio = cursor.fetchone()

    conexion.close()

    if socio:

        resultado.config(
            text=f"""
SOCIO ENCONTRADO

Nombre: {socio[1]}
Apellido: {socio[2]}
CI: {socio[3]}
Teléfono: {socio[4]}
"""
        )

        label_registro.config(
            text=f"Registrado: {socio[5]}"
        )

    else:

        resultado.config(
            text="Socio no encontrado",
            fg="red"
        )


def actualizar():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE socios
        SET nombre=?, apellido=?, telefono=?
        WHERE ci=?
    """, (
        entry_nombre.get(),
        entry_apellido.get(),
        entry_telefono.get(),
        entry_ci.get()
    ))

    conexion.commit()
    conexion.close()

    resultado.config(
        text="Socio actualizado"
    )


def eliminar():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM socios
        WHERE ci=?
    """, (entry_ci.get(),))

    conexion.commit()
    conexion.close()

    limpiar()

    resultado.config(
        text="Socio eliminado"
    )


def limpiar():

    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_ci.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)

    label_registro.config(text="")
    resultado.config(text="")


# ---------------- VENTANA ----------------

def abrir_ventana_socios():

    global entry_nombre
    global entry_apellido
    global entry_ci
    global entry_telefono
    global resultado
    global label_registro

    ventana = tk.Toplevel()

    ventana.title("Gestión de Socios")
    ventana.geometry("500x450")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Nombre").grid(row=0, column=0, pady=5)
    tk.Label(ventana, text="Apellido").grid(row=1, column=0, pady=5)
    tk.Label(ventana, text="CI").grid(row=2, column=0, pady=5)
    tk.Label(ventana, text="Teléfono").grid(row=3, column=0, pady=5)

    entry_nombre = tk.Entry(ventana, width=30)
    entry_apellido = tk.Entry(ventana, width=30)
    entry_ci = tk.Entry(ventana, width=30)
    entry_telefono = tk.Entry(ventana, width=30)

    entry_nombre.grid(row=0, column=1)
    entry_apellido.grid(row=1, column=1)
    entry_ci.grid(row=2, column=1)
    entry_telefono.grid(row=3, column=1)

    tk.Button(
        ventana,
        text="Guardar",
        width=18,
        command=guardar
    ).grid(row=4, column=0, pady=10)

    tk.Button(
        ventana,
        text="Buscar",
        width=18,
        command=buscar
    ).grid(row=4, column=1)

    tk.Button(
        ventana,
        text="Actualizar",
        width=18,
        command=actualizar
    ).grid(row=5, column=0)

    tk.Button(
        ventana,
        text="Eliminar",
        width=18,
        command=eliminar
    ).grid(row=5, column=1)

    tk.Button(
        ventana,
        text="Limpiar",
        width=18,
        command=limpiar
    ).grid(row=6, column=0, columnspan=2, pady=10)

    label_registro = tk.Label(
        ventana,
        text="",
        font=("Arial", 10, "bold")
    )

    label_registro.grid(row=7, column=0, columnspan=2)

    resultado = tk.Label(
        ventana,
        text="",
        font=("Arial", 10, "bold"),
        justify="left"
    )

    resultado.grid(
        row=8,
        column=0,
        columnspan=2,
        pady=10
    )