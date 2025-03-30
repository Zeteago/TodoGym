import flet as ft
from assets.database.operacao import Operacao
from assets.components.twoButtons import AddBackEdit

class TelaVisualizacao:
    def __init__(self, main, treino_id):
        self.main = main
        self.page = main.page
        self.db = Operacao()
        self.treino = self.db.BuscarTreinoCompleto(treino_id)

    def telaVisualizacao(self):
        if not self.treino:
            return ft.Text("Treino não encontrado", color="white")

        print("Renderizando treino:", self.treino)  # Debug print

        exercicios_widgets = []
        for exercicio in self.treino.get("exercicios", []):
            exercicios_widgets.append(self._criar_exercicio(exercicio))

        layout = ft.Container(
            padding=ft.padding.only(left=10, right=10, top=30, bottom=10),
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                value=self.treino["data"],
                                color='white',
                                size=20,
                            ),
                            ft.Text(
                                value=self.treino["nome"],
                                color='white',
                                size=20,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=exercicios_widgets,
                            scroll=ft.ScrollMode.AUTO,
                            spacing=10,
                        ),
                        expand=True,
                        padding=20,
                        border=ft.border.all(1, ft.colors.WHITE)
                    ),
                    AddBackEdit()
                ],
                expand=True
            ),
            expand=True
        )

        return layout

    def _criar_exercicio(self, exercicio):
        print("Criando widget exercício:", exercicio)  # Debug print
        
        series_widgets = []
        for serie in exercicio.get("series", []):
            text = ft.Text(
                value=f"{serie['numero']}ª Série: {serie['repeticoes']} rep - {serie['peso']}kg",
                color='white',
                size=16
            )
            series_widgets.append(text)

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value=exercicio["nome"],
                        color='white',
                        size=18,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Column(
                        controls=series_widgets,
                        spacing=5
                    ),
                    ft.Divider(color='white', height=1)
                ],
                spacing=10
            ),
            padding=10
        )