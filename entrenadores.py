import sqlite3

def registrar_entrenador():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    nombre = input("Nombre del entrenador: ")
    especialidad = input("Especialidad: ")
    telefono = input("Teléfono: ")

    cursor.execute("""
        INSERT INTO entrenadores (nombre, especialidad, telefono)
        VALUES (?, ?, ?)
    """, (nombre, especialidad, telefono))

    conexion.commit()
    conexion.close()
    print("Entrenador registrado correctamente.")


def listar_entrenadores():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, especialidad, telefono
        FROM entrenadores
    """)

    entrenadores = cursor.fetchall()

    if not entrenadores:
        print("No hay entrenadores registrados.")
    else:
        print("\n===== LISTA DE ENTRENADORES =====")
        for entrenador in entrenadores:
            print(
                f"ID: {entrenador[0]} | "
                f"Nombre: {entrenador[1]} | "
                f"Especialidad: {entrenador[2]} | "
                f"Teléfono: {entrenador[3]}"
            )

    conexion.close()


def buscar_entrenador():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    nombre = input("Ingrese el nombre del entrenador: ")

    cursor.execute("""
        SELECT id, nombre, especialidad, telefono
        FROM entrenadores
        WHERE nombre = ?
    """, (nombre,))

    entrenador = cursor.fetchone()

    if entrenador:
        print("\n===== ENTRENADOR ENCONTRADO =====")
        print(f"ID: {entrenador[0]}")
        print(f"Nombre: {entrenador[1]}")
        print(f"Especialidad: {entrenador[2]}")
        print(f"Teléfono: {entrenador[3]}")
    else:
        print("No se encontró el entrenador.")

    conexion.close()


def modificar_entrenador():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    nombre = input("Ingrese el nombre del entrenador a modificar: ")

    cursor.execute("""
        SELECT nombre, especialidad, telefono
        FROM entrenadores
        WHERE nombre = ?
    """, (nombre,))

    entrenador = cursor.fetchone()

    if entrenador:
        print("Deje en blanco si no desea cambiar un dato.")

        nuevo_nombre = input(f"Nombre [{entrenador[0]}]: ")
        nueva_especialidad = input(f"Especialidad [{entrenador[1]}]: ")
        nuevo_telefono = input(f"Teléfono [{entrenador[2]}]: ")

        if nuevo_nombre == "":
            nuevo_nombre = entrenador[0]
        if nueva_especialidad == "":
            nueva_especialidad = entrenador[1]
        if nuevo_telefono == "":
            nuevo_telefono = entrenador[2]

        cursor.execute("""
            UPDATE entrenadores
            SET nombre = ?, especialidad = ?, telefono = ?
            WHERE nombre = ?
        """, (nuevo_nombre, nueva_especialidad, nuevo_telefono, nombre))

        conexion.commit()
        print("Entrenador modificado correctamente.")
    else:
        print("No se encontró el entrenador.")

    conexion.close()


def eliminar_entrenador():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    nombre = input("Ingrese el nombre del entrenador a eliminar: ")

    cursor.execute("""
        SELECT nombre
        FROM entrenadores
        WHERE nombre = ?
    """, (nombre,))

    entrenador = cursor.fetchone()

    if entrenador:
        confirmar = input("¿Está seguro de eliminarlo? (s/n): ")

        if confirmar.lower() == "s":
            cursor.execute("""
                DELETE FROM entrenadores
                WHERE nombre = ?
            """, (nombre,))

            conexion.commit()
            print("Entrenador eliminado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("No se encontró el entrenador.")

    conexion.close()


def menu_entrenadores():
    while True:
        print("\n===== GESTIÓN DE ENTRENADORES =====")
        print("1. Registrar entrenador")
        print("2. Listar entrenadores")
        print("3. Buscar entrenador")
        print("4. Modificar entrenador")
        print("5. Eliminar entrenador")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_entrenador()
        elif opcion == "2":
            listar_entrenadores()
        elif opcion == "3":
            buscar_entrenador()
        elif opcion == "4":
            modificar_entrenador()
        elif opcion == "5":
            eliminar_entrenador()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")