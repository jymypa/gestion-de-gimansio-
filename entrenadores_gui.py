import tkinter as tk
import sqlite3


def conectar():
    return sqlite3.connect("gimnasio.db")


# ---------------- FUNCIONES ----------------

def guardar():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO entrenadores (
            nombre,
            especialidad,
            telefono
        )
        VALUES (?, ?, ?)
    """, (
        entry_nombre.get(),
        entry_especialidad.get(),
        entry_telefono.get()
    ))

    conexion.commit()

    cursor.execute("""
        SELECT * FROM entrenadores
        WHERE nombre = ?
    """, (entry_nombre.get(),))

    entrenador = cursor.fetchone()

    conexion.close()

    if entrenador:

        resultado.config(
            text=f"""
ENTRENADOR REGISTRADO

Nombre: {entrenador[1]}
Especialidad: {entrenador[2]}
Teléfono: {entrenador[3]}
"""
        )


def buscar():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM entrenadores
        WHERE nombre = ?
    """, (entry_nombre.get(),))

    entrenador = cursor.fetchone()

    conexion.close()

    if entrenador:

        resultado.config(
            text=f"""
ENTRENADOR ENCONTRADO

Nombre: {entrenador[1]}
Especialidad: {entrenador[2]}
Teléfono: {entrenador[3]}
"""
        )

    else:

        resultado.config(
            text="Entrenador no encontrado"
        )


def actualizar():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE entrenadores
        SET especialidad=?, telefono=?
        WHERE nombre=?
    """, (
        entry_especialidad.get(),
        entry_telefono.get(),
        entry_nombre.get()
    ))

    conexion.commit()
    conexion.close()

    resultado.config(
        text="Entrenador actualizado"
    )


def eliminar():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM entrenadores
        WHERE nombre=?
    """, (entry_nombre.get(),))

    conexion.commit()
    conexion.close()

    limpiar()

    resultado.config(
        text="Entrenador eliminado"
    )


def mostrar_entrenadores():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM entrenadores
    """)

    entrenadores = cursor.fetchall()

    conexion.close()

    texto = "LISTA DE ENTRENADORES\n\n"

    for entrenador in entrenadores:

        texto += f"""
Nombre: {entrenador[1]}
Especialidad: {entrenador[2]}
Teléfono: {entrenador[3]}

"""

    resultado.config(text=texto)


def limpiar():

    entry_nombre.delete(0, tk.END)
    entry_especialidad.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)

    resultado.config(text="")


# ---------------- VENTANA ----------------

def abrir_ventana_entrenadores():

    global entry_nombre
    global entry_especialidad
    global entry_telefono
    global resultado

    ventana = tk.Toplevel()

    ventana.title("Gestión de Entrenadores")
    ventana.geometry("500x500")
    ventana.resizable(False, False)

    tk.Label(
        ventana,
        text="Nombre"
    ).grid(row=0, column=0, pady=5)

    tk.Label(
        ventana,
        text="TURNO "
    ).grid(row=1, column=0, pady=5)

    tk.Label(
        ventana,
        text="Teléfono"
    ).grid(row=2, column=0, pady=5)

    entry_nombre = tk.Entry(ventana, width=30)
    entry_especialidad = tk.Entry(ventana, width=30)
    entry_telefono = tk.Entry(ventana, width=30)

    entry_nombre.grid(row=0, column=1)
    entry_especialidad.grid(row=1, column=1)
    entry_telefono.grid(row=2, column=1)

    tk.Button(
        ventana,
        text="Guardar",
        width=18,
        command=guardar
    ).grid(row=3, column=0, pady=10)

    
    tk.Button(
        ventana,
        text="Actualizar",
        width=18,
        command=actualizar
    ).grid(row=4, column=0)

    tk.Button(
        ventana,
        text="Eliminar",
        width=18,
        command=eliminar
    ).grid(row=4, column=1)

    tk.Button(
        ventana,
        text="Limpiar",
        width=18,
        command=limpiar
    ).grid(row=5, column=0)

    tk.Button(
        ventana,
        text="Mostrar Entrenadores",
        width=18,
        command=mostrar_entrenadores
    ).grid(row=5, column=1)

    resultado = tk.Label(
        ventana,
        text="",
        font=("Arial", 10, "bold"),
        justify="left"
    )

    resultado.grid(
        row=6,
        column=0,
        columnspan=2,
        pady=15
    )