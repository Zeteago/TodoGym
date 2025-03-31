import flet as ft
from assets.style.estilo import BotaoEstilo

class AddBackEdit(ft.Row):
    def __init__(self, voltar_fun=None, confirmar_fun=None):
        super().__init__(
            controls=[
                ft.ElevatedButton(
                    text="Voltar",
                    style=BotaoEstilo.estilo_vermelho(),
                    expand=True,
                    height=50,
                    on_click=voltar_fun
                ),
                ft.ElevatedButton(
                    text="Confirmar Edição",
                    style=BotaoEstilo.estilo_verde(),
                    expand=True,
                    height=50,
                    on_click=confirmar_fun
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
class AddCancelCria(ft.Row):
    def __init__(self, on_confirmar=None):
        super().__init__(
            controls=[
                ft.ElevatedButton(
                    text="Cancelar",
                    style=BotaoEstilo.estilo_vermelho(),
                    expand=True,
                    height=50,
                    on_click=self._voltar
                ),
                ft.ElevatedButton(
                    text="Confirmar",
                    style=BotaoEstilo.estilo_verde(),
                    expand=True,
                    height=50,
                    on_click=on_confirmar
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

class AddBack(ft.Row):
    def __init__(self, main):
        self.main = main
        self.page = main.page
        super().__init__(
            controls=[
                ft.ElevatedButton(
                    text="Voltar",
                    style=BotaoEstilo.estilo_azul(),
                    expand=True,
                    height=50,
                    on_click=self._voltar
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        

    def _voltar(self, e):
        
        self.page.controls.clear()
        self.main.carregar()
        self.page.update(self.page)