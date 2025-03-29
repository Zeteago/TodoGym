import flet as ft
from assets.database.operacao import Operacao
from assets.components.twoButtons import AddCancelCria
from assets.components.textField import TtextField, NumericField, SeriesField

class TelaAdicionar:
    def __init__(self, main):
        self.main = main
        self.page = main.page

    def telaAdd(self):
        coluna_exercicios = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            spacing=10
        )

        def novos_exercicios(input_field):
            numero = input_field.value
            if not numero.isdigit():
                return
            
            coluna_exercicios.controls.clear()
            
            for i in range(int(numero)):
                container_exercicio = ft.Container(
                    padding=ft.padding.only(left=5, right=5, top=5, bottom=5),
                    content=ft.Column(
                        controls=[
                            ft.ResponsiveRow(
                                columns=3,
                                controls=[
                                    ft.Row(
                                        col=1,
                                        controls=[
                                            ft.Text(
                                                value=f'{i+1}º Exercício',
                                                size=18,
                                                color='white'
                                            )
                                        ],
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                    TtextField('Nome', ''),
                                    NumericField('Séries', text='', mudou=None)
                                ]
                            )
                        ]
                    ),
                    border=ft.Border(
                        top=ft.BorderSide(color=ft.colors.WHITE, width=1),
                        left=ft.BorderSide(color=ft.colors.WHITE, width=1),
                        right=ft.BorderSide(color=ft.colors.WHITE, width=1),
                        bottom=ft.BorderSide(color=ft.colors.WHITE, width=1)
                    ),
                )
                coluna_exercicios.controls.append(container_exercicio)
            
            self.page.update()

        layout = ft.Container(
            padding=ft.padding.only(left=10, right=10, top=30, bottom=10),
            expand=True,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                value='Treino',
                                size=20,
                                color='white'
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Container(
                        expand=True,
                        content=ft.Column(
                            expand=True,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(left=10, right=10, top=10, bottom=10),
                                    expand=True,
                                    content=ft.Column(
                                        expand=True,
                                        controls=[
                                            ft.Container(
                                                padding=ft.padding.only(left=5, right=5, top=5, bottom=5),
                                                content=ft.Column(
                                                    expand=True,
                                                    controls=[
                                                        ft.ResponsiveRow(
                                                            columns=3,
                                                            controls=[
                                                                ft.Row(
                                                                    col=1,
                                                                    controls=[
                                                                        ft.Text(
                                                                            col=1,
                                                                            value='Data',
                                                                            size=18,
                                                                            color='white'
                                                                        ),
                                                                    ],
                                                                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                                                                ),                                                            
                                                                ft.Row(
                                                                    col=2,
                                                                    controls=[
                                                                        ft.ElevatedButton(
                                                                            content=ft.Icon(
                                                                                name=ft.icons.CALENDAR_MONTH,
                                                                                size=30,
                                                                                color='blue'
                                                                            ),
                                                                            bgcolor=ft.colors.GREY_900
                                                                        )
                                                                    ],
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                                                                )
                                                            ]
                                                        ),
                                                        TtextField('Nome', ''),
                                                        NumericField('Exercícios', mudou=novos_exercicios)  
                                                    ]
                                                ),
                                                border=ft.Border(
                                                    top=ft.BorderSide(color=ft.colors.WHITE, width=1),
                                                    left=ft.BorderSide(color=ft.colors.WHITE, width=1),
                                                    right=ft.BorderSide(color=ft.colors.WHITE, width=1),
                                                    bottom=ft.BorderSide(color=ft.colors.WHITE, width=1)
                                                ),
                                            ),
                                            coluna_exercicios
                                        ]
                                    ),
                                    border=ft.Border(
                                        top=ft.BorderSide(color=ft.colors.WHITE, width=1),
                                        left=ft.BorderSide(color=ft.colors.WHITE, width=1),
                                        right=ft.BorderSide(color=ft.colors.WHITE, width=1),
                                        bottom=ft.BorderSide(color=ft.colors.WHITE, width=1)
                                    )
                                )
                            ]
                        )
                    ),
                    AddCancelCria()
                ]
            )
        )

        return self.page.add(layout)
