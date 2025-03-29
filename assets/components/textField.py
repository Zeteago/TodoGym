import flet as ft

class TtextField(ft.ResponsiveRow):
    def __init__(self, value, text, defini=None):

        valor = value if value != '' else ''
        texto = text if text != '' else ''

        super().__init__(
            columns=3,
            controls=[
                ft.Row(
                    col=1,
                    controls=[
                        ft.Text(
                            value=f'{valor}',
                            size=18,
                            color='white'
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Row(
                    col=2,
                    controls=[
                        ft.TextField(
                            value=f'{texto}',
                            expand=True,
                            border_color='white',
                            text_style=ft.TextStyle(
                                color='white'
                            )
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )

class NumericField(ft.ResponsiveRow):
    def __init__(self, value, mudou, text='', defini=None):
        valor = value if value != '' else ''
        texto = text if text != '' else ''
        
        self.coluna_series = ft.Column(
            spacing=5,
            visible=False
        )
        
        self.input_numero = ft.TextField(
            value=f'{texto}',
            expand=True,
            border_color='white',
            text_style=ft.TextStyle(
                color='white'
            )
        )

        def on_series_change(e):
            numero = self.input_numero.value
            if not numero.isdigit():
                return
            
            self.coluna_series.controls.clear()
            self.coluna_series.visible = True
            
            for i in range(int(numero)):
                serie = SeriesField(i + 1)
                self.coluna_series.controls.append(serie)
            
            self.page.update()

        super().__init__(
            columns=3,
            controls=[
                ft.Row(
                    col=1,
                    controls=[
                        ft.Text(
                            value=f'{valor}',
                            size=18,
                            color='white'
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Row(
                    col=2,
                    controls=[
                        self.input_numero,
                        ft.ElevatedButton(
                            content=ft.Icon(
                                name=ft.icons.CONFIRMATION_NUM,
                                size=30,
                                color='blue'
                            ),
                            bgcolor=ft.colors.GREY_900,
                            expand=True,
                            on_click=on_series_change if value == 'Séries' else lambda e: mudou(self.input_numero)
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                self.coluna_series
            ]
        )

class SeriesField(ft.ResponsiveRow):
    def __init__(self, num_serie):
        super().__init__(
            columns=3,
            controls=[
                ft.Row(
                    col=1,
                    controls=[
                        ft.Text(
                            value=f'{num_serie}ª Série',
                            size=16,
                            color='white'
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Row(
                    col=2,
                    controls=[
                        ft.TextField(
                            hint_text="Repetições",
                            expand=True,
                            border_color='white',
                            text_style=ft.TextStyle(
                                color='white'
                            )
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )