import json

class System:
    def add_credentials(self, doctor_instance):
        """
        Adiciona as credenciais de novos funcionários.
        """
        new_credential = {
            'id': doctor_instance.id,
            'name': doctor_instance.name,
            'age': doctor_instance.age,
            'gender': doctor_instance.gender,
            'ocupation': doctor_instance.ocupation,
            'department': doctor_instance.department,
            'is_active': doctor_instance.is_active
        }
        
        archive = 'credentials.json'

        # Carregar credenciais existentes, se houver
        try:
            with open(archive, 'r') as archive:
                existing_credentials = json.load(archive)
        except FileNotFoundError:
            # Se o arquivo não existir, inicialize uma lista vazia de credenciais
            existing_credentials = []

        # Adicionar a nova credencial à lista existente
        existing_credentials.append(new_credential)

        # Escrever a lista atualizada de credenciais em um arquivo JSON
        with open(archive, 'w') as archive_file:
            json.dump(existing_credentials, archive, indent=4)

        print("Credenciais adicionadas com sucesso em", archive)

# sistema = System()
# sistema.add_credentials(100, 'Dra. Harleen F. Quinzel', 'Psiquiatra', 'Instalação Médica', True)
# sistema.add_credentials(101, 'Dr. Jonathan Crane', 'Psiquiatra', 'Instalação Médica', True)