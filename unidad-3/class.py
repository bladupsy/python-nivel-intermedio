class OperacionesM():
		
		def sumar(self, a, b):
				c = a + b
				print("1 :", self)
				print(id(self))
				return c

obj = OperacionesM() #Instancia de la clase
print(obj.sumar(2, 3))
print("1: ", obj)
print(id(obj))