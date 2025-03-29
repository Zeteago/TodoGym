import flet as ft
from assets.database.operacao import Operacao

class TelaVisualizacao:
    def __init__(self, main, info):
        self.main = main
        self.page = main.page
        self.data = info

    def telaVisualizacao(self):

        cards = [
            ['Peito e Tríceps', '29/03/2025'],
            ['Costa e Bíceps', '28/03/2025'],
            ['Perna e Ombro', '27/03/2025'],
        ]

        layout = ft.Container(
            padding=ft.padding.only(left=10, right=10, top=30, bottom=10),
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                value=f'{cards[self.data][1]}',
                                color='white',
                                size=20,
                            ),
                            ft.Text(
                                value=f'{cards[self.data][0]}',
                                color='white',
                                size=20,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ]
            ),
            expand=True
        )

        self.page.update()

        return layout