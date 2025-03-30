import flet as ft
import sqlite3
import os

class Operacao:
    def __init__(self):
        # Remove main and page references
        os.makedirs('assets/db', exist_ok=True)
        self.conn = sqlite3.connect('assets/db/controle_fisico.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self._criar_tabelas()

    def _criar_tabelas(self):
        """Creates all necessary tables with relationships"""
        self.cursor.executescript("""
            CREATE TABLE IF NOT EXISTS Treinos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                nome TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Exercicios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                treino_id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                num_series INTEGER NOT NULL,
                FOREIGN KEY (treino_id) REFERENCES Treinos(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS Series (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                exercicio_id INTEGER NOT NULL,
                numero_serie INTEGER NOT NULL,
                repeticoes INTEGER NOT NULL,
                peso REAL NOT NULL,
                FOREIGN KEY (exercicio_id) REFERENCES Exercicios(id) ON DELETE CASCADE
            );
        """)
        self.conn.commit()

    def InserirTreino(self, nome, data):
        self.cursor.execute(
            "INSERT INTO Treinos (nome, data) VALUES (?, ?)",
            (nome, data)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def InserirExercicio(self, treino_id, nome, num_series):
        self.cursor.execute(
            "INSERT INTO Exercicios (treino_id, nome, num_series) VALUES (?, ?, ?)",
            (treino_id, nome, num_series)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def InserirSerie(self, exercicio_id, numero_serie, repeticoes, peso):
        self.cursor.execute("""
            INSERT INTO Series (exercicio_id, numero_serie, repeticoes, peso) 
            VALUES (?, ?, ?, ?)""",
            (exercicio_id, numero_serie, repeticoes, peso)
        )
        self.conn.commit()

    def AtualizarTreino(self, treino_id, nome, data):
        self.cursor.execute("""
            UPDATE Treinos 
            SET nome = ?, data = ?
            WHERE id = ?
        """, (nome, data, treino_id))
        self.conn.commit()

    def AtualizarExercicio(self):
        pass

    def AtualizarSerie(self):
        pass

    def DeletarTreino(self, treino_id):
        """Deleta treino e cascata"""
        self.cursor.execute("DELETE FROM Treinos WHERE id = ?", (treino_id,))
        self.conn.commit()

    def DeletarExercicio(self):
        pass

    def DeletarSerie(self):
        pass

    def BuscarTreinos(self):
        self.cursor.execute("""
            SELECT id, nome, data FROM Treinos 
            ORDER BY data DESC
        """)
        return self.cursor.fetchall()

    def BuscarTreinoCompleto(self, treino_id):
        try:
            self.cursor.execute("""
                SELECT 
                    t.id as treino_id, 
                    t.nome as treino_nome,
                    t.data,
                    e.id as exercicio_id,
                    e.nome as exercicio_nome,
                    s.numero_serie,
                    s.repeticoes,
                    s.peso
                FROM Treinos t
                LEFT JOIN Exercicios e ON e.treino_id = t.id
                LEFT JOIN Series s ON s.exercicio_id = e.id
                WHERE t.id = ?
                ORDER BY e.id, s.numero_serie
            """, (treino_id,))
            
            rows = self.cursor.fetchall()
            
            if not rows:
                return None
                
            # Format the result
            treino = {
                "id": rows[0][0],
                "nome": rows[0][1],
                "data": rows[0][2],
                "exercicios": []
            }
            
            current_exercicio = None
            for row in rows:
                # If we have exercise data and it's a new exercise
                if row[3] is not None and (current_exercicio is None or current_exercicio["id"] != row[3]):
                    current_exercicio = {
                        "id": row[3],
                        "nome": row[4],
                        "series": []
                    }
                    treino["exercicios"].append(current_exercicio)
                
                # If we have series data
                if row[5] is not None and current_exercicio is not None:
                    current_exercicio["series"].append({
                        "numero": row[5],
                        "repeticoes": row[6],
                        "peso": row[7]
                    })
            
            print("Treino formatado:", treino)  # Debug print
            return treino
            
        except Exception as e:
            print(f"Erro ao buscar treino: {e}")
            return None

    def _formatar_resultado(self, rows):
        """Formats database results into a nested dictionary"""
        if not rows:
            return None

        treino = {
            "id": rows[0][0],
            "data": rows[0][1],
            "nome": rows[0][2],
            "exercicios": []
        }

        exercicio_atual = None
        for row in rows:
            if row[3] and (not exercicio_atual or exercicio_atual["id"] != row[3]):
                exercicio_atual = {
                    "id": row[3],
                    "nome": row[4],
                    "num_series": row[5],
                    "series": []
                }
                treino["exercicios"].append(exercicio_atual)
            
            if row[6]:  # if has series data
                exercicio_atual["series"].append({
                    "numero": row[6],
                    "repeticoes": row[7],
                    "peso": row[8]
                })

        return treino
