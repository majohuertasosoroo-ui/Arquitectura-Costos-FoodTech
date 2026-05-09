import sqlite3
from Backend.database import DB_NAME

class ControlCostos:
    @staticmethod
    def guardar_costo(ingrediente, p_anterior, p_actual, inflacion, alerta):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO costos (ingrediente, precio_anterior, precio_actual, inflacion, alerta)
                VALUES (?, ?, ?, ?, ?)
            ''', (ingrediente, p_anterior, p_actual, inflacion, alerta))
            conn.commit()