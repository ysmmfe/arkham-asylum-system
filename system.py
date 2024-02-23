from class_modules import Doctor
class System:
    def __init__(self):
        self.credentials = {}
    
    def add_credentials(self, doctor_instance):
        """
        Adiciona as credenciais de novos funcionários.
        """
        new_credential = {
            'name': doctor_instance.name,
            'age': doctor_instance.age,
            'gender': doctor_instance.gender,
            'specialization': doctor_instance.specialization,
            'crm': doctor_instance.crm,
            'is_active': doctor_instance.is_active,
            'department': doctor_instance.department
        }
        
        self.credentials[doctor_instance.id] = new_credential
        print(self.credentials)
        
    def search_credential(self, id):
        """
        Obtém as credenciais associadas a um código.
        Retorna None se o código não estiver presente nas credenciais.
        """
        if id in self.credentials:
            return self.credentials[id]
        else:
            return None