import PySimpleGUI as sg

# All the stuff inside my window
layout_menu = [
    [sg.Text("==== Menu ====", key='menu')],
    [sg.Button('1. Adicionar funcionário'), sg.Button('Sair do Menu')]
]

# Layout da tela "Adicionar um funcionário"
layout_add_employee = [
                    [sg.Text("Adicionando funcionário:\n")],
                    [sg.Text("ID:"), sg.Input(size=(6, 1)), sg.Text("Nome:"), sg.Input(size=(35, 1))],
                    [sg.Text("Idade:"), sg.Input(size=(6, 1)), sg.Text("Gênero:"), sg.Input(size=(31, 1))],
                    [sg.Text("Ocupação:"), sg.Input(size=(20, 1)), sg.Text("Está ativo?"), sg.Input(size=(10, 1))],
                    [sg.Text("Departamento:"), sg.Input(size=(40, 1))],
                    [sg.Text("\n")],
                    [sg.Button("Adicionar"), sg.Button("Voltar para o menu")]
                ]
