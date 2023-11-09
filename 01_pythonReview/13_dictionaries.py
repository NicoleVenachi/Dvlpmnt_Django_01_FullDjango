
#  Creación diccionarios con curly brackest ---> {'key': value,...} | or | dict constructor ---> dict({'key': value,...}) 
my_dict = {
  'name': 'Juan',
  'age': 25,
  'is_tall': True,
  'city': 'Madrid',
  'friends': ['Peter', 'Paul', 'John', 'Ana']
}

# Inddexacion (con [])
print(my_dict)
print(my_dict['name'])

# overwriting
my_dict['name'] = 'Diana'
print(my_dict['name'])

#methods to apply to a dictionary
print(len(my_dict)) # me dice cuantos elementos tengo
print(type(my_dict)) #tipo de la estructura de datos