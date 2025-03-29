import flet as ft

class BotaoEstilo:
    @staticmethod
    def estilo_azul():
        return ft.ButtonStyle(
            bgcolor={
                ft.ControlState.DEFAULT: 'blue'
            },
            color={
                ft.ControlState.DEFAULT: 'white'
            },
            shape={
                ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=0)
            },
            side={
                ft.ControlState.DEFAULT: ft.BorderSide(width=1, color='blue')
            }
        )
    
    def estilo_verde():
        return ft.ButtonStyle(
            bgcolor={
                ft.ControlState.DEFAULT: 'green'
            },
            color={
                ft.ControlState.DEFAULT: 'white'
            },
            shape={
                ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=0)
            },
            side={
                ft.ControlState.DEFAULT: ft.BorderSide(width=1, color='green')
            }
        )
    
    def estilo_vermelho():
        return ft.ButtonStyle(
            bgcolor={
                ft.ControlState.DEFAULT: 'red'
            },
            color={
                ft.ControlState.DEFAULT: 'white'
            },
            shape={
                ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=0)
            },
            side={
                ft.ControlState.DEFAULT: ft.BorderSide(width=1, color='red')
            }
        )
