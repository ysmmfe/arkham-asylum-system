# Programa de Penitenciária - Arkham Asylum

class SistemaAutenticacao:
    def __init__(self):
        # Cria um dicionário para armazenar credenciais dos funcionários associadas aos códigos
        self.credenciais = {}


    def adicionar_credenciais(self, codigo, username, ocupacao, setor, ativo):
        """
        Adiciona as credenciais dos funcionários.
        """
        nova_credencial = {
            'username': username,
            'ocupacao': ocupacao,
            'setor': setor,
            'ativo': ativo
        }
        
        self.credenciais[codigo] = nova_credencial


    def obter_credenciais_por_codigo(self, codigo):
        """
        Obtém as credenciais associadas a um código.
        Retorna None se o código não estiver presente nas credenciais.
        """
        return self.credenciais.get(codigo)


    def autenticar_usuario(self, codigo):
        """
        Autentica um usuário com base no código fornecido.
        Retorna True se o usuário for autenticado, False caso contrário.
        """
        informacoes_credenciais = self.obter_credenciais_por_codigo(codigo)

        if informacoes_credenciais and informacoes_credenciais['ativo'] is True:
            print(f"\nBem-vindo, {informacoes_credenciais['username']}!")
            return True
        else:
            print("Código inválido. Tente novamente.")
            return False
        
class SistemaCriminosos:
    def __init__(self):
        # Cria um dicionário para armazenar as credenciais dos criminosos insanos
        self.criminosos = {}
        
    def adicionar_ficha_criminal(self, codigo, name, alias, situation, crimes):
        """
        Adiciona as informações às fichas dos criminosos insanos.
        """
        nova_ficha_criminal = {
            'name': name,
            'alias': alias,
            'situation': situation,
            'crimes': crimes
        }
        
        self.criminosos[codigo] = nova_ficha_criminal
    
    def obter_ficha_por_codigo(self, codigo):
        """
        Obtém a ficha criminosa associadas a um código.
        Retorna None se o código não estiver presente no sistema.
        """
        return self.criminosos.get(codigo)
    
    def mostrar_ficha_criminal(self, codigo):
        self.codigo = codigo
        ficha_criminal = self.obter_ficha_por_codigo(codigo)
        
        if ficha_criminal:
            print("==================================")
            print(f"Ficha criminal - Criminoso {self.codigo}:")
            print("==================================")
            print(f"> NAME: {ficha_criminal['name']}")
            print(f"> ALIASES: {ficha_criminal['alias']}")
            print(f"> SITUATION: {ficha_criminal['situation']}")
            print(f"> REGISTRED CRIMES:\n{ficha_criminal['crimes']}")
            print("==================================")
            return True # Ficha criminal encontrada
        else:
            print("Código inválido! Tente novamente.")
            return False

def main():

    while True:
        try:
            codigo = int(input("Digite seu código de acesso: "))
            if sistema_autenticacao.autenticar_usuario(codigo):
                # O usuário foi autenticado, podemos continuar com as operações necessárias
                break
        except ValueError:
            print("Por favor, insira um número válido.")
            
    while True:
        try:
            print("\n==== Menu Principal ====\n1 - Puxar ficha criminal\n2 - Sair do Menu")
            opcao = int(input("\nInforme a opção desejada: "))
            
            match opcao:
                # 1 - Puxar ficha criminal
                case 1:
                    codigo_ficha = int(input("Digite o código do criminoso: "))
                    sistema_criminosos.mostrar_ficha_criminal(codigo_ficha)
                    continue
                    
                case 2:
                    break
        except ValueError:
            print("Por favor, insira um número válido.")
            

# Adicionando credenciais para funcionários
sistema_autenticacao = SistemaAutenticacao()
sistema_autenticacao.adicionar_credenciais(100, 'Dra. Harleen F. Quinzel', 'Psiquiatra', 'Instalação Médica', True)
sistema_autenticacao.adicionar_credenciais(101, 'Dr. Jonathan Crane', 'Psiquiatra', 'Instalação Médica', True)

# Adicionando fichas de criminosos
sistema_criminosos = SistemaCriminosos()
sistema_criminosos.adicionar_ficha_criminal(200, 'Martin Hawkins', 'Mad Dog', 'Prisoner', 'Targeted, murdered and sexually abused women.')
            
# Executando o main
if __name__ == "__main__":
    main()