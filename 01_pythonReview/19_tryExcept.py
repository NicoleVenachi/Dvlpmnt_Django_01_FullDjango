
# *** Sintaxis try/except ***

# En forma generl
try:
  x = int(input('Input an integer value: \t'))
  print(x)

except ValueError:
  print('Invalid input, value must be an integer... Please try again')

except:
  print('Something went wrong')

else:
  print('Nothing went wrong')

finally:
  print('Try-except finished')


try:
  x = int(input('Input an integer value: \t'))
  print(x)
except ValueError: 
  print('Invalid input, value must be an integer... Please try again')

  