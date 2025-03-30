import flet as ft
from assets.database.operacao import Operacao
from assets.components.twoButtons import AddCancelCria
from assets.components.textField import TtextField, NumericField, SeriesField
from datetime import datetime
from assets.components.exercicio_container import ExercicioContainer

class TelaAdicionar:
    def __init__(self, main):
        self.main = main
        self.page = main.page
        self.db = Operacao(self)
        self.exercicios_containers = []

    def salvar_treino(self, e):
        try:
            # Pega data atual
            data = datetime.now().strftime("%d/%m/%Y")
            
            # Pega nome do treino
            nome_treino = self._get_nome_treino()
            
            # Insere treino e pega ID
            treino_id = self.db.InserirTreino(nome_treino, data)
            
            # Para cada container de exercício
            for container in self.exercicios_containers:
                # Pega dados do exercício
                nome_exercicio = container.get_nome_exercicio()
                series = container.get_series()
                
                if nome_exercicio and series:
                    # Insere exercício e pega ID
                    exercicio_id = self.db.InserirExercicio(treino_id, nome_exercicio)
                    
                    # Insere cada série
                    for num, serie in enumerate(series, 1):
                        self.db.InserirSerie(
                            exercicio_id,
                            num,
                            serie["repeticoes"],
                            serie["peso"]
                        )
            
            # Volta para tela inicial
            self.page.controls.clear()
            self.main.carregar()
            self.page.update()
            
        except Exception as e:
            print(f"Erro ao salvar treino: {e}")

    def _get_nome_treino(self):
        nome_field = self.page.controls[0].content.controls[1].content.controls[0].content.controls[0].content.controls[1]
        return nome_field.controls[1].controls[0].value

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
            self.exercicios_containers.clear()
            
            for i in range(int(numero)):
                container = ExercicioContainer(i+1)
                coluna_exercicios.controls.append(container)
                self.exercicios_containers.append(container)
            
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
                    AddCancelCria(on_confirmar=self.salvar_treino)
                ]
            )
        )

        return self.page.add(layout)
