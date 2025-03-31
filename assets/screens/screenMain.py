import flet as ft
from assets.database.operacao import Operacao
from assets.components.botao import AddButtonSimpleAzul, AddButtonSimpleVerde, AddButtonSimpleVermelho
from assets.components.botao import CardTreino

class TelaInicial:
    def __init__(self, main):
        self.main = main
        self.page = main.page
        self.db = Operacao()

    def carregar_treinos(self):
        try:
            treinos = self.db.BuscarTreinos()
            cards = []
            
            for treino in treinos:
                card = CardTreino(
                    self.main,
                    nome_treino=treino[1],
                    data=treino[2],
                    id=treino[0]
                )
                cards.append(card)
                
            return cards if cards else [
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text("Nenhum treino cadastrado", 
                            color="white", 
                            size=16,
                            text_align=ft.TextAlign.CENTER
                            ),
                        ],
                        expand=True,
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    expand=True
                )
            ]
        except Exception as e:
            print(f"Erro ao carregar treinos: {e}")
            return []
    
    def voltar(self, e):
        from assets.screens.screenAdd import TelaAdicionar
        self.page.controls.clear()
        self.tela_adicionar = TelaAdicionar(self)
        self.tela_adicionar.telaAdd()

    def carregar(self):
        """Recarrega a tela inicial com os treinos atualizados"""
        self.page.controls.clear()
        self.PrimeiraTela()
        self.page.update()

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
                                height=50,
                                fun=self.voltar
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
