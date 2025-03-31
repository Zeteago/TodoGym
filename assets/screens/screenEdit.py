import flet as ft
from datetime import datetime
from assets.database.operacao import Operacao
from assets.style.estilo import BotaoEstilo
from assets.components.twoButtons import AddBackEdit

class TelaEdicao:
    def __init__(self, main, treino_id):
        self.main = main
        self.page = main.page
        self.db = Operacao()
        self.treino_id = treino_id
        self.nome_treino = None
        self.exercicios_containers = []
        
        # Carrega dados do treino existente
        self.treino_data = self.db.BuscarTreinoCompleto(treino_id)

    def atualizar_series(self, e, series_column):
        """Atualiza o número de séries de um exercício"""
        if not e.control.value.isdigit():
            return
            
        num_series = int(e.control.value)
        series_column.controls.clear()
        
        for i in range(num_series):
            series_column.controls.append(
                self.criar_serie_field(i+1)
            )
        
        self.page.update()

    def criar_serie_field(self, num, repeticoes="", peso="", series_column=None):
        return ft.Row(
            controls=[
                ft.Text(f"{num}ª Série", size=16, color='white', width=80),
                ft.TextField(
                    value=str(repeticoes),
                    hint_text="Repetições",
                    border_color='white',
                    keyboard_type=ft.KeyboardType.NUMBER,
                    width=50
                ),
                ft.Text("rep", size=16, color='white', width=30),
                ft.TextField(
                    value=str(peso),
                    hint_text="Peso",
                    border_color='white',
                    keyboard_type=ft.KeyboardType.NUMBER,
                    width=50
                ),
                ft.Text("kg", size=16, color='white', width=30),
                ft.IconButton(
                    icon=ft.icons.DELETE,
                    icon_color="red",
                    tooltip="Excluir série",
                    on_click=lambda e: self.excluir_serie(series_column, num-1)
                )
            ]
        )

    def criar_exercicio_container(self, numero, exercicio=None):
        series_column = ft.Column([], spacing=5)
        
        container = ft.Container(
            padding=10,
            content=ft.Column([
                # Cabeçalho do exercício com nome e botão deletar
                ft.Row([
                    ft.TextField(
                        value=exercicio["nome"] if exercicio else "",
                        hint_text=f"Nome do Exercício {numero}",
                        border_color='white',
                        expand=True
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color="red",
                        tooltip="Excluir exercício",
                        on_click=lambda e, ex_id=exercicio["id"] if exercicio else None: 
                            self.excluir_exercicio(e, ex_id, container)
                    )
                ]),
                # Controles de séries - Removido campo de número de séries
                ft.Row([
                    ft.Text("Séries:", color="white"),
                    ft.IconButton(
                        icon=ft.icons.ADD_CIRCLE,
                        icon_color="blue",
                        tooltip="Adicionar série",
                        on_click=lambda e: self.adicionar_serie(series_column)
                    )
                ]),
                series_column
            ]),
            border=ft.border.all(1, ft.colors.WHITE)
        )
        
        # Preenche séries existentes
        if exercicio and exercicio.get("series"):
            for i, serie in enumerate(exercicio["series"]):
                series_column.controls.append(
                    self.criar_serie_field(i+1, serie["repeticoes"], serie["peso"], series_column)
                )
        
        return container

    def coletar_dados_treino(self):
        exercicios = []
        
        for container in self.exercicios_containers:
            # O nome está no primeiro TextField dentro da primeira Row
            nome_field = container.content.controls[0].controls[0]
            
            exercicio = {
                'nome': nome_field.value,
                'series': []
            }
            
            # As séries estão na última Column
            series_column = container.content.controls[2]
            for serie in series_column.controls:
                exercicio['series'].append({
                    'repeticoes': serie.controls[1].value,  # TextField de repetições
                    'peso': serie.controls[3].value         # TextField de peso
                })
                
            exercicios.append(exercicio)
            
        return exercicios

    def atualizar_treino(self, e):
        """Atualiza o treino no banco quando clica em Confirmar Edição"""
        nome_treino = self.nome_treino.value
        
        if not nome_treino:
            return

        try:
            # Obtém dados atualizados da interface
            treino_atualizado = {
                'id': self.treino_id,
                'nome': nome_treino,
                'data': datetime.now().strftime("%d/%m/%Y"),
                'exercicios': self.coletar_dados_treino()
            }
            
            # Atualiza nome e data do treino
            self.db.AtualizarTreino(self.treino_id, treino_atualizado['nome'], treino_atualizado['data'])
            
            # Obtém exercícios existentes
            exercicios_existentes = self.db.BuscarExerciciosPorTreino(self.treino_id)
            
            # Atualiza exercícios existentes e adiciona novos
            for exercicio in treino_atualizado['exercicios']:
                exercicio_existente = next(
                    (ex for ex in exercicios_existentes if ex['nome'] == exercicio['nome']), 
                    None
                )
                
                if exercicio_existente:
                    # Atualiza exercício existente
                    self.db.AtualizarExercicio(
                        exercicio_existente['id'],
                        exercicio['nome']
                    )
                    
                    # Atualiza/adiciona séries
                    series_existentes = self.db.BuscarSeriesPorExercicio(exercicio_existente['id'])
                    
                    for i, serie in enumerate(exercicio['series'], 1):
                        if i <= len(series_existentes):
                            # Atualiza série existente
                            self.db.AtualizarSerie(
                                series_existentes[i-1]['id'],
                                serie['repeticoes'],
                                serie['peso']
                            )
                        else:
                            # Adiciona nova série
                            self.db.InserirSerie(
                                exercicio_existente['id'],
                                i,
                                serie['repeticoes'],
                                serie['peso']
                            )
                    
                    # Remove séries excedentes
                    for serie in series_existentes[len(exercicio['series']):]:
                        self.db.DeletarSerie(serie['id'])
                        
                else:
                    # Adiciona novo exercício com suas séries
                    exercicio_id = self.db.InserirExercicio(
                        self.treino_id,
                        exercicio['nome'],
                        len(exercicio['series'])
                    )
                    
                    for i, serie in enumerate(exercicio['series'], 1):
                        self.db.InserirSerie(
                            exercicio_id,
                            i,
                            serie['repeticoes'],
                            serie['peso']
                        )
            
            # Remove exercícios que não existem mais
            for ex in exercicios_existentes:
                if not any(e['nome'] == ex['nome'] for e in treino_atualizado['exercicios']):
                    self.db.DeletarExercicio(ex['id'])
            
            # Volta para tela principal
            self.page.controls.clear()
            self.main.carregar()
            self.page.update()
                
        except Exception as e:
            print(f"Erro ao atualizar treino: {e}")

    def telaEdicao(self):
        self.coluna_exercicios = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            spacing=10
        )

        # Campo para nome do treino com valor preenchido
        self.nome_treino = ft.TextField(
            value=self.treino_data["nome"],
            label="Nome do Treino",
            border_color="white",
            text_size=16
        )

        # Preenche exercícios existentes
        for i, exercicio in enumerate(self.treino_data["exercicios"]):
            container = self.criar_exercicio_container(i+1, exercicio)
            self.exercicios_containers.append(container)
            self.coluna_exercicios.controls.append(container)

        # Substitua o bloco de botões por:
        botoes = AddBackEdit(
            voltar_fun=lambda e: self.voltar(),
            confirmar_fun=self.atualizar_treino
        )

        # Adiciona botão de novo exercício
        layout = ft.Container(
            padding=ft.padding.only(left=10, right=10, top=30, bottom=10),
            content=ft.Column(
                controls=[
                    ft.Text("Editar Treino", size=30, color="white"),
                    self.nome_treino,
                    ft.Row([
                        ft.Text("Exercícios:", color="white", size=20),
                        ft.IconButton(
                            icon=ft.icons.ADD_CIRCLE,
                            icon_color="blue",
                            tooltip="Adicionar exercício",
                            on_click=self.adicionar_exercicio
                        )
                    ]),
                    self.coluna_exercicios,
                    botoes
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
        self.page.update(self.page)

    def excluir_serie(self, series_column, index):
        """Remove uma série visualmente e atualiza a numeração"""
        try:
            series_column.controls.pop(index)
            # Atualiza numeração das séries restantes
            for i, serie in enumerate(series_column.controls):
                serie.controls[0].value = f"{i+1}ª Série"
            self.page.update()  # Atualiza apenas visualmente
        except Exception as e:
            print(f"Erro ao excluir série: {e}")

    def excluir_exercicio(self, e, exercicio_id, container):
        """Exclui um exercício e atualiza a tela"""
        try:
            if exercicio_id:
                self.db.DeletarExercicio(exercicio_id)
            self.exercicios_containers.remove(container)
            self.page.controls.clear()
            self.telaEdicao()
        except Exception as e:
            print(f"Erro ao excluir exercício: {e}")

    def adicionar_serie(self, series_column):
        """Adiciona uma nova série visualmente ao exercício"""
        try:
            num_serie = len(series_column.controls) + 1
            nova_serie = self.criar_serie_field(
                num=num_serie,
                series_column=series_column
            )
            series_column.controls.append(nova_serie)
            self.page.update()  # Atualiza apenas visualmente
        except Exception as e:
            print(f"Erro ao adicionar série: {e}")

    def adicionar_exercicio(self, e):
        """Adiciona um novo exercício visualmente ao treino"""
        try:
            num_exercicio = len(self.exercicios_containers) + 1
            container = self.criar_exercicio_container(num_exercicio)
            self.exercicios_containers.append(container)
            self.coluna_exercicios.controls.append(container)
            self.page.update()  # Atualiza apenas visualmente
        except Exception as e:
            print(f"Erro ao adicionar exercício: {e}")