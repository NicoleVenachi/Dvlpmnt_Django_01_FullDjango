
print('Create account now')
username = input('Enter username: \t')
password = input('Enter password: \t')

print('Your account has been created successfully')
print('Login now!')

username2 = input('Enter username: \t')
password2 = input('Enter password: \t')

if ((username == username2) and (password == password2)):
  print('Logged in successfully')
else:
  print('Invalid credentials')
