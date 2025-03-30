import flet as ft
import sqlite3

class Operacao:
    def __init__(self, main):
        self.main = main
        self.page = main.page

        # Conexão com o banco de dados SQLite
        self.conn = sqlite3.connect('assets/db/controle_fisico.db')
        self.cursor = self.conn.cursor()

        # Criação da tabela se não existir
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Treinos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                nome TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def InserirTreino(self, nome, data):
        self.cursor.execute(
            "INSERT INTO Treinos (nome, data) VALUES (?, ?)",
            (nome, data)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def InserirExercicio(self, treino_id, nome):
        self.cursor.execute(
            "INSERT INTO Exercicios (treino_id, nome) VALUES (?, ?)",
            (treino_id, nome)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def InserirSerie(self, exercicio_id, numero_serie, repeticoes, peso):
        self.cursor.execute(
            "INSERT INTO Series (exercicio_id, numero_serie, repeticoes, peso) VALUES (?, ?, ?, ?)",
            (exercicio_id, numero_serie, repeticoes, peso)
        )
        self.conn.commit()

    def AtualizarTreino(self):
        pass

    def AtualizarExercicio(self):
        pass

    def AtualizarSerie(self):
        pass

    def DeletarTreino(self):
        pass

    def DeletarExercicio(self):
        pass

    def DeletarSerie(self):
        pass
