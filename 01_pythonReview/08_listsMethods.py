
list1 = [4, 3, 5, 1, 2]
list2 = ['banana', 'apple', 'mango', 'orange']

# *** Métodos que MUTAN el array original***

list1.sort() #ordenar lista
print(list1)
list2.reverse()# invertir orden de la lista
print(list2)
list1.extend(list2) #join/concatenar lsitas
print(list1)
list1.append('cherry') #agregar elemento al final
print(list1)
list1.insert(1, 'kiwi')# (idx, newElem) instertar elemento en un lugar deseado(medio similar a splice de JS)
print(list1)
list1.pop() # eliminar último elemento
print(list1)
list1.pop(1) # eliminar elemento por su idx
print(list1)
del list1[1] # eliminar elemento por su idx (built-in methods)
print(list1)
list1.remove('banana') # eliminar element por su valor
print(list1)
list1.clear()# elimnar todos los elementos en la lsita, limpiarlo, dejarlo vacio
print(list1)
del list1 # elimino completamente la lista


# *** Métodos que NO MUTAN el array original***

print(list2.index('mango')) # encontrar el index de un elemento (indexing by value)
print(list2.count('mango')) # contar el numero de apariciones

