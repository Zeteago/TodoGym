import flet as ft
from .textField import TtextField, NumericField, SeriesField

class ExercicioContainer(ft.Container):
    def __init__(self, numero):
        super().__init__()
        self.padding = ft.padding.only(left=5, right=5, top=5, bottom=5)
        self.series_containers = []
        
        self.nome_exercicio = TtextField(f'Exercício {numero}', '')
        
        def on_series_change(e):
            num_series = e.control.value
            if not num_series.isdigit():
                return
                
            self.atualizar_series(int(num_series))
        
        self.content = ft.Column(
            controls=[
                self.nome_exercicio,
                NumericField('Séries', mudou=lambda x: on_series_change(x))
            ]
        )
        
        self.border = ft.border.all(1, ft.colors.WHITE)

    def atualizar_series(self, num_series):
        series_column = ft.Column(spacing=5)
        self.series_containers.clear()
        
        for i in range(num_series):
            serie = SeriesField(i+1)
            series_column.controls.append(serie)
            self.series_containers.append(serie)
            
        if len(self.content.controls) > 2:
            self.content.controls.pop()
        self.content.controls.append(series_column)
        self.update()

    def get_nome_exercicio(self):
        """Returns exercise name"""
        return self.nome_exercicio.get_valor()

    def get_series(self):
        """Returns list of series data"""
        return [serie.get_dados() for serie in self.series_containers]