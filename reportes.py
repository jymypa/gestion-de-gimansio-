import sqlite3

def mostrar_reporte_general():
    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM socios")
    total_socios = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM entrenadores")
    total_entrenadores = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM pagos")
    total_pagos = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(monto) FROM pagos")
    resultado = cursor.fetchone()[0]

    if resultado is None:
        ingresos_acumulados = 0
    else:
        ingresos_acumulados = resultado

    print("\n===== REPORTE GENERAL =====")
    print(f"Total de clientes : {total_socios}")
    print(f"Total de entrenadores: {total_entrenadores}")
    print(f"Total de pagos registrados: {total_pagos}")
    print(f"Ingresos acumulados: Bs. {ingresos_acumulados:.2f}")

    conexion.close()


def menu_reportes():
    while True:
        print("\n===== REPORTES =====")
        print("1. Mostrar reporte general")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_reporte_general()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            