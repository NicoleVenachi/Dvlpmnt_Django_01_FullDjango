
# *** For sintaxis ***

# over a string
for letter in 'Hello':
  print(letter)

# over a list
myList = ['ji', 'ju', 'jo']

for element in myList:

  if element == 'ji':
    continue # skip
  elif element == 'ju':
    pass  # does nothing
  else:
    break # finishes the iteration

  
  print(element) #toma cada value

# over a dictionary
myDict = {
  'name': 'jhon',
  'age': 25	
}

for element in myDict:
  print(element) #toma cada key

# over a list of numbers
for element in range(10):
  print(element)
else:
  print('finished looping')

  