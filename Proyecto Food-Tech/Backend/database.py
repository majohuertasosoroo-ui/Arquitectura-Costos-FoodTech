import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "foodtech_costos.db")

def inicializar_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS costos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ingrediente TEXT,
                precio_anterior REAL,
                precio_actual REAL,
                inflacion REAL,
                alerta TEXT
            )
        ''')
        conn.commit()