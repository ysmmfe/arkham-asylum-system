from .Person import Person

class Prisioner(Person):
    def __init__(self, id, name, age, gender, alias, crime, entry_date):
        super().__init__(name, age, gender) # Função chama o método init da classe base e passa os parâmetros,
                                            # garantindo que os atributos da classe base sejam inicializados corretamente.
        self.id = id
        self.alias = alias
        self.crime = crime
        self.entry_date = entry_date
        
    def record_visits(self):
        pass
    
    def check_status(self):
        pass