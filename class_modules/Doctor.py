from .Person import Person

class Doctor(Person):
    def __init__(self, id, name, age, gender, specialization, crm, is_active=True, department="Instalação Médica"):
        super().__init__(name, age, gender)
        
        self.id = id
        self.specialization = specialization
        self.crm = crm
        self.is_active = is_active
        self.department = department