import sqlite3
from datetime import datetime, timedelta

def registrar_pago():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    ci = input("Ingrese el CI del socio: ")

    cursor.execute("""
        SELECT id, nombre, apellido
        FROM socios
        WHERE ci = ?
    """, (ci,))

    socio = cursor.fetchone()

    if not socio:
        print("No se encontró el socio.")
        conexion.close()
        return

    print(f"Socio: {socio[1]} {socio[2]}")

    monto = float(input("Monto pagado: "))
    fecha_pago = datetime.now().strftime("%Y-%m-%d")
    fecha_vencimiento = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")

    cursor.execute("""
        INSERT INTO pagos (socio_id, monto, fecha_pago, fecha_vencimiento)
        VALUES (?, ?, ?, ?)
    """, (socio[0], monto, fecha_pago, fecha_vencimiento))

    conexion.commit()
    conexion.close()

    print("Pago registrado correctamente.")
    print(f"Fecha de vencimiento: {fecha_vencimiento}")


def listar_pagos():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT s.nombre, s.apellido, p.monto, p.fecha_pago, p.fecha_vencimiento
        FROM pagos p
        INNER JOIN socios s ON p.socio_id = s.id
        ORDER BY p.fecha_pago DESC
    """)

    pagos = cursor.fetchall()

    if not pagos:
        print("No hay pagos registrados.")
    else:
        print("\n===== LISTA DE PAGOS =====")
        for pago in pagos:
            print(
                f"Socio: {pago[0]} {pago[1]} | "
                f"Monto: Bs. {pago[2]} | "
                f"Fecha Pago: {pago[3]} | "
                f"Vencimiento: {pago[4]}"
            )

    conexion.close()


def menu_pagos():
    while True:
        print("\n===== GESTIÓN DE PAGOS =====")
        print("1. Registrar pago")
        print("2. Listar pagos")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_pago()
        elif opcion == "2":
            listar_pagos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")