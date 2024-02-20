import PySimpleGUI as sg
from class_modules import Doctor
from system import System
from gui import layout_menu, layout_add_employee

def main():
    system = System()
            
    # Create the Window
    window = sg.Window('Arkham Asylum System', layout_menu)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == "Sair do Menu":
            break
        
        if event == "1. Adicionar funcionário":
            new_window = sg.Window('Arkham Asylum System', layout_add_employee)

            while True:
                new_event, new_value = new_window.read()
                
                # if user closes window or clicks cancel
                if new_event == sg.WIN_CLOSED or new_event == "Voltar para o menu":
                    new_window.close()
                    break
                        
                if new_event == "Adicionar":
                    system.add_credentials(Doctor(new_value[0], new_value[1], new_value[2], new_value[3], new_value[4], new_value[6], answer))
                    sg.popup("Funcionário adicionado com sucesso!")

    window.close()
    

# Executando o main
if __name__ == "__main__":
    main()