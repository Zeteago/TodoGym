import flet as ft
from datetime import datetime
from assets.database.operacao import Operacao
from assets.components.botao import AddButtonSimpleAzul 
from assets.style.estilo import BotaoEstilo

class TelaAdicionar:
    def __init__(self, main):
        self.main = main
        self.page = main.page
        self.db = Operacao()
        self.nome_treino = None
        self.exercicios_containers = []
        
        # Dicionário para armazenar dados do treino
        self.treino_data = {
            'nome': '',
            'data': '',
            'exercicios': []
        }

    def coletar_dados_treino(self):
        exercicios = []
        
        # Percorre cada container de exercício
        for container in self.exercicios_containers:
            exercicio = {
                'nome': container.content.controls[0].value,
                'series': []
            }
            
            # Percorre as séries do exercício
            series_column = container.content.controls[2]
            for serie in series_column.controls:
                exercicio['series'].append({
                    'repeticoes': serie.controls[1].controls[0].value,
                    'peso': serie.controls[2].controls[0].value
                })
                
            exercicios.append(exercicio)
            
        return exercicios

    def salvar_treino(self, e):
        # Coleta nome do treino
        nome_treino = self.nome_treino.value
        
        if not nome_treino:
            self.page.snack_bar = ft.SnackBar(content=ft.Text("Nome do treino é obrigatório"))
            self.page.snack_bar.open = True
            self.page.update()
            return

        # Atualiza dados do treino
        self.treino_data = {
            'nome': nome_treino,
            'data': datetime.now().strftime("%d/%m/%Y"),
            'exercicios': self.coletar_dados_treino()
        }

        # Salva no banco de dados
        try:
            self.db.inserir_treino(self.treino_data)
            self.page.snack_bar = ft.SnackBar(content=ft.Text("Treino salvo com sucesso!"))
            self.page.snack_bar.open = True
            self.page.update()
            
            # Limpa a tela e volta para tela principal
            self.page.controls.clear()
            self.main.carregar()
            self.page.update()
        except Exception as e:
            self.page.snack_bar = ft.SnackBar(content=ft.Text(f"Erro ao salvar: {str(e)}"))
            self.page.snack_bar.open = True
            self.page.update()

    def criar_serie_field(self, num):
        return ft.ResponsiveRow(
            columns=5,
            controls=[
                ft.Row(col=1, controls=[ft.Text(f"{num}ª Série", size=16, color='white')]),
                ft.Row(col=1, controls=[ft.TextField(hint_text="Repetições", border_color='white', width=50, keyboard_type=ft.KeyboardType.NUMBER)]),
                ft.Row(col=1, controls=[ft.Text("rep", size=16, color='white')]),
                ft.Row(col=1, controls=[ft.TextField(hint_text="Peso (kg)", border_color='white', width=50, keyboard_type=ft.KeyboardType.NUMBER)]),
                ft.Row(col=1, controls=[ft.Text("kg", size=16, color='white')])
            ]
        )

    def criar_exercicio_container(self, numero):
        container = ft.Container(
            padding=10,
            content=ft.Column([
                ft.TextField(hint_text=f"Nome do Exercício {numero}", border_color='white'),
                ft.ResponsiveRow(
                    columns=2,
                    controls=[ 
                        ft.Row(col=1, controls=[ft.Text("Número de séries", size=18, color="white"),]),
                        ft.Row(col=1, controls=[ft.TextField(
                            hint_text="Quantidade",
                            border_color='white',
                            on_change=lambda e: self.atualizar_series(e, series_column), 
                            keyboard_type=ft.KeyboardType.NUMBER
                        ),])
                    ]
                ),
                ft.Column([], spacing=5) # series_column
            ]),
            border=ft.border.all(1, ft.colors.WHITE)
        )
        series_column = container.content.controls[-1]
        return container

    def atualizar_series(self, e, series_column):
        if not e.control.value.isdigit():
            return
        num_series = int(e.control.value)
        series_column.controls.clear()
        for i in range(num_series):
            series_column.controls.append(self.criar_serie_field(i+1))
        self.page.update()

    def telaAdd(self):
        coluna_exercicios = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            spacing=10
        )

        # Campo para nome do treino
        self.nome_treino = ft.TextField(
            label="Nome do Treino",
            border_color="white",
            text_size=16
        )

        def novos_exercicios(e):
            if not e.control.value.isdigit():
                return
                
            num = int(e.control.value)
            coluna_exercicios.controls.clear()
            self.exercicios_containers.clear()
            
            for i in range(num):
                container = self.criar_exercicio_container(i+1)
                self.exercicios_containers.append(container)
                coluna_exercicios.controls.append(container)
                
            self.page.update()

        botoes = ft.Row(
            controls=[
                AddButtonSimpleAzul(
                    text="Voltar",
                    inf="voltar",
                    height=50,
                    fun=lambda e: self.voltar(),
                    expand=True
                ),
                ft.ElevatedButton(
                    text="Salvar",
                    on_click=self.salvar_treino,
                    style=BotaoEstilo.estilo_verde(),
                    expand=True,
                    height=50
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        layout = ft.Container(
            padding=ft.padding.only(left=10, right=10, top=30, bottom=10),
            content=ft.Column(controls=[
                ft.Text("Novo Treino", size=30, color="white"),
                self.nome_treino,
                ft.ResponsiveRow(
                    columns=2,
                    controls=[ 
                        ft.Text("Número de exercícios", size=18, color="white"),
                        ft.TextField(
                            label="Quantidade",
                            border_color="white",
                            on_change=novos_exercicios, 
                            keyboard_type=ft.KeyboardType.NUMBER
                        ),
                    ]
                ),
                coluna_exercicios,
                botoes  # Adicione os botões ao layout
            ],
            scroll=ft.ScrollMode.HIDDEN,
            expand=True
            ),
            expand=True
        )

        return self.page.add(layout)

    def voltar(self):
        self.page.controls.clear()
        self.main.carregar()
        self.page.update()
