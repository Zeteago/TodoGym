import flet as ft
from assets.database.operacao import Operacao
from assets.components.botao import AddButtonSimpleAzul, AddButtonSimpleVerde, AddButtonSimpleVermelho
from assets.components.botao import CardTreino

class TelaInicial:
    def __init__(self, main):
        self.main = main
        self.page = main.page

    def carregar_treinos(self):
        # Busca todos os treinos do banco
        # treinos = self.operacao.buscar_todos_treinos()
        cards = [
            CardTreino(self.main, 'Peito e Tríceps', '29/03/2025', 0),
            CardTreino(self.main, 'Costa e Bíceps', '28/03/2025', 1),
            CardTreino(self.main, 'Perna e Ombro', '27/03/2025', 2),
        ]
        
        # for treino in treinos:
        #     card = CardTreino(
        #         nome_treino=treino['nome'],
        #         data=treino['data']
        #     )
        #     cards.append(card)
            
        return cards

    def PrimeiraTela(self):
        
        layout = ft.Container(
            padding=ft.padding.only(left=10, right=10, top=30, bottom=10),
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                "Treino", 
                                size=30, 
                                color=ft.colors.WHITE
                                )
                            ], 
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Container(
                        padding=ft.padding.only(left=10, right=10, top=10, bottom=0),
                        content=ft.Column(
                            spacing=15,
                            controls=self.carregar_treinos(),
                            expand=True,
                            scroll=ft.ScrollMode.HIDDEN
                        ),
                        expand=True,
                        border=ft.Border(
                            top=ft.BorderSide(color=ft.colors.WHITE, width=1),
                            left=ft.BorderSide(color=ft.colors.WHITE, width=1),
                            right=ft.BorderSide(color=ft.colors.WHITE, width=1),
                            bottom=ft.BorderSide(color=ft.colors.WHITE, width=1)
                        )
                    ),
                    ft.Row(
                        controls=[
                            AddButtonSimpleAzul(
                                text="Novo",
                                inf="adiciona",
                                width=200,
                                height=50
                            )
                        ], 
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ]
            ),
            expand=True
        )

        self.page.add(layout)


# CREATE TABLE Exercicios (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     treino_id INTEGER NOT NULL,
#     nome TEXT NOT NULL,
#     FOREIGN KEY (treino_id) REFERENCES Treinos(id) ON DELETE CASCADE
# );

# CREATE TABLE Series (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     exercicio_id INTEGER NOT NULL,
#     serie INTEGER NOT NULL,
#     repeticoes INTEGER NOT NULL,
#     FOREIGN KEY (exercicio_id) REFERENCES Exercicios(id) ON DELETE CASCADE
# );
