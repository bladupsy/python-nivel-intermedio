class OperacionesM():
    variable = ""
    @staticmethod
    def sumar(cls, a, b):
        c = a + b
        print(cls.variable)
        return c
    
obj = OperacionesM()

print(obj.sumar(2, 3))
print(OperacionesM.sumar(2, 3))