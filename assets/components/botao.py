import flet as ft
from assets.database.operacao import Operacao
from assets.style.estilo import BotaoEstilo
from assets.screens.screenView import TelaVisualizacao

class AddButtonSimpleAzul(ft.ElevatedButton):
    def __init__(self, text, inf, width=30, height=30, expand=False, fun=None):
        super().__init__(
            text=text,
            data=inf,
            style=BotaoEstilo.estilo_azul(),
            width=width,
            height=height,
            expand=expand,
            on_click=fun
        )

class AddButtonSimpleVerde(ft.ElevatedButton):
    def __init__(self, text, inf, width=30, height=30, expand=False, fun=None):
        super().__init__(
            text=text,
            data=inf,
            style=BotaoEstilo.estilo_verde(),
            width=width,
            height=height,
            expand=expand,
            on_click=fun
        )

class AddButtonSimpleVermelho(ft.ElevatedButton):
    def __init__(self, text, inf, width=30, height=30, expand=False, fun=None):
        super().__init__(
            text=text,
            data=inf,
            style=BotaoEstilo.estilo_vermelho(),
            width=width,
            height=height,
            expand=expand,
            on_click=fun
        )

class CardTreino(ft.Container):
    def __init__(self, main, nome_treino="Nome do Treino", data="DD-MM-YYYY", id=None):
        self.main = main
        self.page = main.page
        self.id = id
        self.db = Operacao()
        
        def deletar_treino(e):
            try:
                # Deleta o treino do banco (CASCADE irá deletar exercícios e séries)
                self.db.DeletarTreino(self.id)
                # Recarrega a tela principal
                self.page.controls.clear()
                
                from assets.screens.screenMain import TelaInicial
                self.page.controls.clear()
                self.tela_inicial = TelaInicial(self)
                self.tela_inicial.PrimeiraTela()
            except Exception as e:
                print(f"Erro ao deletar treino: {e}")

        super().__init__(
            content=ft.Container(
                padding=ft.padding.only(left=5, right=5, top=5, bottom=5),
                content=ft.Column(
                    spacing=5,
                    controls=[
                        ft.Row(
                            expand=True,
                            controls=[
                                ft.Text(
                                    data,
                                    color=ft.colors.WHITE,
                                    size=20,
                                ),
                                AddButtonSimpleVermelho(
                                    text="X",
                                    inf="deletar",
                                    fun=deletar_treino
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            expand=True,
                            controls=[
                                ft.Text(
                                    nome_treino,
                                    color=ft.colors.WHITE,
                                    size=20,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            vertical_alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            expand=True,
                            controls=[
                                AddButtonSimpleVerde(
                                    text="Visualizar",
                                    inf="visualizar",
                                    expand=True,
                                    fun=lambda e: (
                                        self.page.controls.clear(),
                                        self.page.add(TelaVisualizacao(self.main, id).telaVisualizacao())
                                    )
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    expand=True
                ),
                expand=True,
                border=ft.Border(
                    top=ft.BorderSide(color='white', width=1),
                    bottom=ft.BorderSide(color='white', width=1),
                    left=ft.BorderSide(color='white', width=1),
                    right=ft.BorderSide(color='white', width=1),
                )
            )
        )
