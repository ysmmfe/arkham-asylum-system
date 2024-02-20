from .Person import Person

class Visitor(Person):
    def __init__(self, name, age, gender, id_prisioner, relationship, date_and_time):
        super().__init__(name, age, gender)
        
        self.id_prisioner = id_prisioner
        self.relationship = relationship
        self.date_and_time = date_and_time