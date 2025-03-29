import flet as ft
from assets.style.estilo import BotaoEstilo

class AddBackEdit(ft.Row):
    def __init__(self, on_voltar=None, on_editar=None):

        def muda(e):
            from assets.screens.screenMain import TelaInicial
            self.page.controls.clear()
            self.tela_inicial = TelaInicial(self)
            self.tela_inicial.PrimeiraTela()

        super().__init__(
            controls = [
                ft.ElevatedButton(
                    text="Voltar",
                    style=BotaoEstilo.estilo_azul(),
                    expand=True,
                    height=50,
                    on_click=muda
                ),
                ft.ElevatedButton(
                    text="Editar",
                    style=BotaoEstilo.estilo_azul(),
                    expand=True,
                    height=50,
                    on_click=muda
                )
            ],
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
class AddCancelCria(ft.Row):
    def __init__(self, on_voltar=None, on_editar=None):

        def telaInicio(e):
            from assets.screens.screenMain import TelaInicial
            self.page.controls.clear()
            self.tela_inicial = TelaInicial(self)
            self.tela_inicial.PrimeiraTela()

        super().__init__(
            controls = [
                ft.ElevatedButton(
                    text="Voltar",
                    style=BotaoEstilo.estilo_vermelho(),
                    expand=True,
                    height=50,
                    on_click=telaInicio
                ),
                ft.ElevatedButton(
                    text="Confirmar",
                    style=BotaoEstilo.estilo_azul(),
                    expand=True,
                    height=50,
                    on_click=telaInicio
                )
            ],
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        )