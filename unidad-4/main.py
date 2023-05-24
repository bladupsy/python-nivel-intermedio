class Personas():
    def __init__(self, nombre, edad, salario, trabajo=None) :
        self.nombre = nombre
        self.salario = salario
        self.edad = edad
        self.trabajo = trabajo

juan=Personas("Juan", 7, 500)
susana=Personas("Susana", 8, 400)

print(juan.nombre)
print(susana.edad)