import flet as ft

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

class SeriesContainer(ft.Column):
    def __init__(self):
        super().__init__(
            spacing=5,
            visible=False
        )
        
    def atualizar_series(self, numero):
        if not numero.isdigit():
            return
            
        self.controls.clear()
        self.visible = True
        
        for i in range(int(numero)):
            serie = SeriesField(i + 1)
            self.controls.append(serie)