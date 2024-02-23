import flet as ft
from system import System
from gui import PageManager

def main(page: ft.Page):
    system = System()
    page_manager = PageManager(system)
    
    page.title = "Arkham Asylum System"
    page.vertical_alignment = ft.MainAxisAlignment

    page_manager.main_menu_page(page)

# Executando o main
if __name__ == "__main__":
    ft.app(target=main)