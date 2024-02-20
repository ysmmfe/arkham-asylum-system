from .Person import Person

class Doctor(Person):
    def __init__(self, id, name, age, gender, ocupation, department, is_active):
        super().__init__(name, age, gender)
        
        self.id = id
        self.ocupation = ocupation
        self.department = department
        self.is_active = is_active
        
        