import sqlite3

def registrar_socio():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    ci = input("CI: ")
    telefono = input("Teléfono: ")
    fecha_registro = input("Fecha de registro (YYYY-MM-DD): ")

    try:
        cursor.execute("""
            INSERT INTO socios (nombre, apellido, ci, telefono, fecha_registro)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, apellido, ci, telefono, fecha_registro))

        conexion.commit()
        print("Socio registrado correctamente.")
    except sqlite3.IntegrityError:
        print("El CI ya está registrado.")

    conexion.close()


def listar_socios():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, apellido, ci, telefono, estado FROM socios")
    socios = cursor.fetchall()

    if not socios:
        print("No hay socios registrados.")
    else:
        print("\n===== LISTA DE SOCIOS =====")
        for socio in socios:
            print(
                f"ID: {socio[0]} | "
                f"Nombre: {socio[1]} {socio[2]} | "
                f"CI: {socio[3]} | "
                f"Teléfono: {socio[4]} | "
                f"Estado: {socio[5]}"
            )

    conexion.close()


def buscar_socio():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    ci = input("Ingrese el CI del socio: ")

    cursor.execute("""
        SELECT id, nombre, apellido, ci, telefono, estado
        FROM socios
        WHERE ci = ?
    """, (ci,))

    socio = cursor.fetchone()

    if socio:
        print("\n===== SOCIO ENCONTRADO =====")
        print(f"ID: {socio[0]}")
        print(f"Nombre: {socio[1]} {socio[2]}")
        print(f"CI: {socio[3]}")
        print(f"Teléfono: {socio[4]}")
        print(f"Estado: {socio[5]}")
    else:
        print("No se encontró ningún socio con ese CI.")

    conexion.close()


def modificar_socio():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    ci = input("Ingrese el CI del socio a modificar: ")

    cursor.execute("""
        SELECT nombre, apellido, telefono
        FROM socios
        WHERE ci = ?
    """, (ci,))

    socio = cursor.fetchone()

    if socio:
        print("Deje en blanco si no desea cambiar un dato.")

        nuevo_nombre = input(f"Nombre [{socio[0]}]: ")
        nuevo_apellido = input(f"Apellido [{socio[1]}]: ")
        nuevo_telefono = input(f"Teléfono [{socio[2]}]: ")

        if nuevo_nombre == "":
            nuevo_nombre = socio[0]
        if nuevo_apellido == "":
            nuevo_apellido = socio[1]
        if nuevo_telefono == "":
            nuevo_telefono = socio[2]

        cursor.execute("""
            UPDATE socios
            SET nombre = ?, apellido = ?, telefono = ?
            WHERE ci = ?
        """, (nuevo_nombre, nuevo_apellido, nuevo_telefono, ci))

        conexion.commit()
        print("Socio modificado correctamente.")
    else:
        print("No se encontró ningún socio con ese CI.")

    conexion.close()


def eliminar_socio():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    ci = input("Ingrese el CI del socio a eliminar: ")

    cursor.execute("SELECT nombre, apellido FROM socios WHERE ci = ?", (ci,))
    socio = cursor.fetchone()

    if socio:
        print(f"Socio encontrado: {socio[0]} {socio[1]}")
        confirmar = input("¿Está seguro de eliminarlo? (s/n): ")

        if confirmar.lower() == "s":
            cursor.execute("DELETE FROM socios WHERE ci = ?", (ci,))
            conexion.commit()
            print("Socio eliminado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("No se encontró ningún socio con ese CI.")

    conexion.close()


def menu_socios():
    while True:
        print("\n===== GESTIÓN DE SOCIOS =====")
        print("1. Registrar socio")
        print("2. Listar socios")
        print("3. Buscar socio por CI")
        print("4. Modificar socio")
        print("5. Eliminar socio")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_socio()
        elif opcion == "2":
            listar_socios()
        elif opcion == "3":
            buscar_socio()
        elif opcion == "4":
            modificar_socio()
        elif opcion == "5":
            eliminar_socio()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")