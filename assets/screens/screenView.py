import flet as ft
from assets.database.operacao import Operacao
from assets.components.twoButtons import AddBackEdit

class TelaVisualizacao:
    def __init__(self, main, info):
        self.main = main
        self.page = main.page
        self.data = info

    def telaVisualizacao(self):

        cards = [
            ['Peito e Tríceps', '29/03/2025', 5],
            ['Costa e Bíceps', '28/03/2025', 4],
            ['Perna e Ombro', '27/03/2025', 6],
        ]

        exercicios = [
            ['Supino', 3],
            ['PeckDeck', 3],
            ['Crossover', 3]
        ]

        rep = [
            [15, 12, 10],
            [12, 8, 8],
            [12, 10, 8]
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
                    ),
                    ft.Container(
                        content=ft.Container(
                            expand=True,
                            padding=ft.padding.only(left=20, right=20, top=20, bottom=0),
                            content=ft.Column(
                                controls=[
                                    ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        value=f'{v[0]}',
                                                        color='white',
                                                        size=18
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.START
                                            ),
                                            ft.Column(
                                                controls=[
                                                    ft.Row(
                                                        controls=[
                                                            ft.Text(
                                                                value=f'{num+1}° Série: {val[n]}',
                                                                color='white',
                                                                size=16
                                                            )
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER
                                                    ) for num, val in enumerate(rep)
                                                ]
                                            ),
                                            ft.Divider(
                                                color='white',
                                                height=1
                                            )
                                        ] 
                                    ) for n, v in enumerate(exercicios)
                                ]
                            ) 
                        ),
                        expand=True,
                        border=ft.Border(
                            top=ft.BorderSide(color=ft.colors.WHITE, width=1),
                            left=ft.BorderSide(color=ft.colors.WHITE, width=1),
                            right=ft.BorderSide(color=ft.colors.WHITE, width=1),
                            bottom=ft.BorderSide(color=ft.colors.WHITE, width=1)
                        )
                    ),
                    AddBackEdit()
                ]
            ),
            expand=True
        )

        return layout