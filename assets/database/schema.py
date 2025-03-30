import sqlite3
import os

def criar_banco():
    # Garante que o diretório db existe
    os.makedirs('assets/db', exist_ok=True)
    
    conn = sqlite3.connect('assets/db/todo_gym.db')
    cursor = conn.cursor()

    # Habilita foreign keys
    cursor.execute("PRAGMA foreign_keys = ON")

    # Cria as tabelas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Treinos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Exercicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            treino_id INTEGER NOT NULL,
            nome TEXT NOT NULL,
            FOREIGN KEY (treino_id) REFERENCES Treinos(id) ON DELETE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Series (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercicio_id INTEGER NOT NULL,
            numero_serie INTEGER NOT NULL,
            repeticoes INTEGER NOT NULL,
            peso REAL NOT NULL DEFAULT 0,
            FOREIGN KEY (exercicio_id) REFERENCES Exercicios(id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()