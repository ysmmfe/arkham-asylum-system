import flet as ft
from class_modules import Doctor

class PageManager:
    def __init__(self, system):
        self.system = system
        
    def main_menu_page(self, page):
        page.add(ft.Text("===== Menu Principal ====="),
                    ft.ElevatedButton(text="1. Adicionar funcionário", on_click=lambda _: self.add_credentials_page(page)),
                    ft.ElevatedButton(text="2. Procurar credenciais", on_click=lambda _: self.search_id_page(page)),
                    # Futuro botão para fechar a janela
                    #ft.ElevatedButton(text="Sair do menu", on_click=)
                    )
    
    def return_to_menu(self, page):
        page.clean()
        self.main_menu_page(page)
            
    def add_credentials_page(self, page):
        page.clean()
        page.add(ft.Text(value="Preencha todos os campos abaixo: "))
    
        id = ft.TextField(label="ID")
        name = ft.TextField(label="Full Name")
        age = ft.TextField(label="Age")
        gender = ft.TextField(label="Gender")
        specialization = ft.TextField(label="Specialization")
        crm = ft.TextField(label="CRM")
        
        page.add(id, name, age, gender, specialization, crm)
        
        def add_doctor(_):
            id_value = id.value
            name_value = name.value
            age_value = age.value
            gender_value = gender.value
            specialization_value = specialization.value
            crm_value = crm.value
            
            try:
                self.system.add_credentials(Doctor(id_value, name_value, age_value, gender_value, specialization_value, crm_value))
                page.add(ft.Text(f"\n{name_value} adicionada com sucesso!"))
            except Exception as e:
                page.add(ft.Text(f"Erro ao adicionar credenciais: "))
            
        page.add(ft.Row(controls=[
            ft.ElevatedButton(text="Adicionar", on_click=add_doctor),
            ft.ElevatedButton(text="Voltar para o Menu", on_click=lambda _: self.return_to_menu(page))
        ]))
    
    # Futura implementação
    # def search_id_page(self, page):
    #     page.clean()