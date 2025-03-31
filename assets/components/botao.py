import flet as ft
from assets.database.operacao import Operacao
from assets.style.estilo import BotaoEstilo
from assets.screens.screenView import TelaVisualizacao
from assets.screens.screenEdit import TelaEdicao

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

        def fechar_dialogo():
            self.caixa_confirma.open = False  #FECHA O DIALOGO
            self.page.update(self.page)

        def popup(e):
            self.caixa_confirma = ft.AlertDialog(
                modal=True, #ATIVAR
                title=ft.Text('Por favor, confirme.', color='white'), #FRASE PRINCIPAL
                content=ft.Text('Tem certeza que deseja excluir?', color='white'), #EXPLICAÇÃO
                actions=[ #ESCOLHAS DA CAIXA DE DIÁLOGO
                    ft.TextButton('Sim', on_click=deletar_treino, data=e.control.data, style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: 'blue'})),
                    ft.TextButton('Não', on_click=lambda e: fechar_dialogo(), style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: 'blue'}))
                ],
                actions_alignment=ft.MainAxisAlignment.END, #POSICIONAMENTO DAS OPC,
                bgcolor='black'
            )
            self.page.open(self.caixa_confirma)
        
        def deletar_treino(e):
            try:
                # Deleta o treino do banco (CASCADE irá deletar exercícios e séries)
                self.db.DeletarTreino(self.id)
                # Recarrega a tela principal
                fechar_dialogo()
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
                                    fun=popup
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
                                AddButtonSimpleAzul(
                                    text="Visualizar",
                                    inf="visualizar",
                                    expand=True,
                                    fun=lambda e: (
                                        self.page.controls.clear(),
                                        self.page.add(TelaVisualizacao(self.main, id).telaVisualizacao())
                                    )
                                ),
                                AddButtonSimpleVerde(
                                    text="Editar",
                                    inf="editar",
                                    expand=True,
                                    fun=lambda e: (
                                        self.page.controls.clear(),
                                        TelaEdicao(self.main, self.id).telaEdicao()
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
