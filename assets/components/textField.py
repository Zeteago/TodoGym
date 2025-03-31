import flet as ft
from .series_field import SeriesField  # Importar a classe do arquivo correto

class TtextField(ft.ResponsiveRow):
    def __init__(self, value, text, defini=None):
        valor = value if value != '' else ''
        texto = text if text != '' else ''
        
        # Guardar referência do TextField
        self.input_field = ft.TextField(
            value=f'{texto}',
            expand=True,
            border_color='white',
            text_style=ft.TextStyle(
                color='white'
            )
        )

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
                        self.input_field  # Usar a referência aqui
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )

    def get_valor(self):
        return self.input_field.value

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
            ),
            keyboard_type=ft.KeyboardType.NUMBER
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

    def get_valor(self):
        return self.input_numero.value