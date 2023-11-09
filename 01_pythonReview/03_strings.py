
name = 'tim'

# *** Strings review****
print('Hi, \n how \\are  u\' ') #line break
print(name)

# *** Strings methods review****
print(name[0]) #index first letter (iterable)
print(name.upper()) #string a MAYUSCULAS
print(name.lower()) #string a minusculas

print(name.islower())#check if EVERYTHING is lowercase
print(name.isupper())#check if EVERYTHING is uppercase

print(name.upper().islower())#concateneting funcionts

print(len(name))# built-in method to check iterable length

print(name.index('im'))# get INDEX of a pattern
print(name.replace('im', 'eam')) #(pattern, toReplace) reemplazo el patrón en la cadena, con el elemento enviado