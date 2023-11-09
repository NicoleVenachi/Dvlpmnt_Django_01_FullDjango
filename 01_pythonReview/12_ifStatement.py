

#  **** Sintanxis ***
a = 2
b = 3

if (a < b): #(condicion)
  #body
  print(str(a) + ' is greater than ' + str(b))

elif (a == b):
  print(str(a) +' is equal to '+ str(b))

else:
  print(str(a) +' is less than '+ str(b))


# **** Simple example (check the input argument)****

value = bool(input('Input a value: \t'))

if type(value) == str:
  print(str(value) +' is a string')

elif type(value) == int:
  print(str(value) +' is an integer')

elif type(value) == list:
  print(str(value) + 'is a list')

else:
  print('We don\'t know the data type of: \t' + str(value))

# **** Simple example (check if a number can be divided by 5)****

value = int(input('Input a numer: \t'))

if ((value % 5) == 0):
  print('Number ' + str(value) + ' can be divided by 5')

else:
  print('Number ' + str(value) + ' can not be divided by 5')

# **** Simple example (check if a sentence length is less than 10)****

value = input('Input a sentence: \t')

if (len(value) < 10):
  print(str(value) +' is less than 10')
else:
  print(str(value) +' is greater than 10')