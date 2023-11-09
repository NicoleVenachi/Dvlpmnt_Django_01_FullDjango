
# ******** Crear/Definir functions  ********

def function_name(parameters):
  a = parameters
  pass # cuerpo de la funcion

# def greetings_function(*name):
#   print(type(name)) #name -> tuple
#   print('Welcome ' + name[1])

# greetings_function('perro', 'tim', 'diana') # para *args

def greetings_function(name, age):
  print('Welcome ' + name + ' you\'re ' + str(age) + 'years old')

# ******** llamar/invocar function ********
function_name('arguments')

# greetings_function('perro', 23) #directo
# greetings_function(name= 'perro', age =23) #precedidos

name = input('Enter your name: \t')
age = input('Enter your age: \t')
greetings_function(name, age) #con varaibles

