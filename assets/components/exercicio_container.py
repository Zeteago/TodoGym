import flet as ft
from .textField import TtextField, NumericField, SeriesField

class ExercicioContainer(ft.Container):
    def __init__(self, numero):
        super().__init__()
        self.padding = ft.padding.only(left=5, right=5, top=5, bottom=5)
        self.series_containers = []
        
        def on_series_change(e):
            self.atualizar_series(e.control.value)
        
        self.content = ft.Column(
            controls=[
                ft.ResponsiveRow(
                    columns=3,
                    controls=[
                        ft.Row(
                            col=1,
                            controls=[
                                ft.Text(
                                    value=f'{numero}º Exercício',
                                    size=18,
                                    color='white'
                                )
                            ],
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        TtextField('Nome', ''),
                        NumericField('Séries', text='', mudou=on_series_change)
                    ]
                ),
                ft.Column(  # Container para as séries
                    controls=[],
                    spacing=5
                )
            ]
        )
        
        self.border = ft.Border(
            top=ft.BorderSide(color=ft.colors.WHITE, width=1),
            left=ft.BorderSide(color=ft.colors.WHITE, width=1),
            right=ft.BorderSide(color=ft.colors.WHITE, width=1),
            bottom=ft.BorderSide(color=ft.colors.WHITE, width=1)
        )

    def atualizar_series(self, numero):
        if not numero.isdigit():
            return
            
        series_column = self.content.controls[1]
        series_column.controls.clear()
        self.series_containers.clear()
        
        for i in range(int(numero)):
            serie = SeriesField(i+1)
            series_column.controls.append(serie)
            self.series_containers.append(serie)
        
        self.update()

    def get_nome_exercicio(self):
        return self.content.controls[0].controls[1].get_valor()

    def get_series(self):
        return [container.get_dados() for container in self.series_containers]