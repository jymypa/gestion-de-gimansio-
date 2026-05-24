import sqlite3

def crear_base_datos():

    conexion = sqlite3.connect("gimnasio.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            ci TEXT UNIQUE NOT NULL,
            telefono TEXT,
            fecha_registro TEXT,
            estado TEXT DEFAULT 'Activo'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entrenadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            especialidad TEXT,
            telefono TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rutinas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pagos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            socio_id INTEGER,
            monto REAL NOT NULL,
            fecha_pago TEXT,
            fecha_vencimiento TEXT,
            FOREIGN KEY (socio_id) REFERENCES socios(id)
        )
    """)

    conexion.commit()
    conexion.close()

    print("Base de datos creada correctamente.")


if __name__ == "__main__":
    crear_base_datos()