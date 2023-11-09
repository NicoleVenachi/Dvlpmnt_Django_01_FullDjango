
# open(filename, 'mode')
# Modes ----> -(r)eading, -(w)rite, -(a)ppend to the end of the file,  -(r+) reand andd write capabilities

countr_file = open('./countries.txt', 'r') # abrir the file

print(countr_file.readable()) # saber si el file es leible (permisos)

print(countr_file.readline()) # leo linea a lina, una a una (queda almacenado ultima leida, header queda alli para proxima lectura)

print(countr_file.readlines()) # devuelvo todas las líneas en una list (un list element por cada linea)

countr_file.seek(0,0) #reset a first line

for line in countr_file.readlines():
  print(line)

countr_file.close()# cerrar the file

