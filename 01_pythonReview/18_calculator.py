
num1 = int(input('Enter first number: \t'))
num2 = int(input('Enter second number: \t'))
op = input('Enter operator: \t')

if op == '+':
  print('The addition is: \t', num1 + num2)
elif op == '-':
  print('The substraction is: \t', num1 - num2)
elif op == '*':
  print('The multiplication is: \t', num1 * num2)
elif op == '/':
  print('The division is: \t', num1 / num2)
else:
  print('Invalid operator')
