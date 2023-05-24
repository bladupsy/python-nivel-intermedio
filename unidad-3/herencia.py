
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
    

    def comer_arroz(self):
        print("Comer arroz desde persona")
    
class Cultura(): pass
class Koreanos(Persona, Cultura):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer_arroz(self):
        print("Comer arroz desde Korea")


class Argentinos(Persona, Cultura):
    def __init__(self, nombre):
        self.nombre = nombre
    
    #Polimosfirmo
    def comer_arroz(self):
        print("Comer arroz desde Argentina")


anna = Persona("Anna Karen")
juan = Persona("Juan Emilio")
pepita = Argentinos("Josefa Emilia")
josefa = Koreanos("Josefa Jacinta")
anna.comer_arroz()
juan.comer_arroz()
josefa.comer_arroz()
pepita.comer_arroz()

#Nos indica en que clase estados y de donde hereda las respuestas
print(Koreanos.__mro__)