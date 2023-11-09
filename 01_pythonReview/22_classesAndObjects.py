
# Creo clase
class Person:
  def __init__(self, name, age):
    # constructor (for received arguments)
    self.name = name
    self.age = age
  
  #default arguments

# Creo objeto
#name = input('Entr you name: \t')
#age = input('Entr you age: \t')

person1 = Person('Isabela', '30') # cinstancia de la clase

#accesar atributos/métodos dle objeto
print(person1.name) 

#puedo eliminar atributos 
del person1.name
print(type(person1))

