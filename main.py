from database import crear_base_datos
from socios import menu_socios
from entrenadores import menu_entrenadores
from pagos import menu_pagos   
from reportes import menu_reportes  

def mostrar_menu(): 
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE GIMNASIO =====")
        print("1. Gestionar clientes")
        print("2. Gestionar entrenadores")
        print("3. Gestionar pagos")
        print("4. Reportes")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_socios()
        elif opcion == "2":
            menu_entrenadores()
        elif opcion == "3":
            menu_pagos()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "0":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    crear_base_datos()
    mostrar_menu()