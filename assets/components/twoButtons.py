import flet as ft
from assets.style.estilo import BotaoEstilo


class AddBackEdit(ft.Row):
    def __init__(self, on_voltar=None, on_editar=None):

        def voltar(e):
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
                    on_click=voltar
                ),
                ft.ElevatedButton(
                    text="Editar",
                    style=BotaoEstilo.estilo_azul(),
                    expand=True,
                    height=50,
                    on_click=on_editar
                )
            ],
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        )
        

