import flet as ft
from assets.screens.screenMain import TelaInicial

class Main:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Controle Físico"
        page.bgcolor = ft.colors.GREY_900

        self.tela_inicial = TelaInicial(self)

        self.carregar()

    def carregar(self):
        
        self.tela_inicial.PrimeiraTela()

ft.app(target=Main, assets_dir='assets')