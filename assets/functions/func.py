import flet as ft
import sqlite3
import os

os.makedirs('assets/db', exist_ok=True)
conn = sqlite3.connect('assets/db/controle_fisico.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

for c in range(66, 70):
    cursor.execute(f"DELETE FROM Exercicios WHERE id = {c}")
    conn.commit()