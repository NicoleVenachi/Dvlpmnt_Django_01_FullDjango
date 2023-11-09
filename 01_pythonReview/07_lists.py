
#creacion square brackest ---> [elems,..] | or | list constructor ---> list((elems,...))
countries = ['United Kingdom', 'Ghana', 'Nigeria', 'Australia', 7, 'New Zeeland', 8, True] #list creation []
countries2 = list((1,2, 'Colombia hpta')) #list creation constructor
print(countries)
print(countries2)


#indexing
print(countries[1]) #indexing list
print(countries[1][1]) #indexing the inner element (string is a iterable)
print(countries[-1]) #indexing al revés


#slices [start:end:steps]
print(countries[1:])  # till' the end
print(countries[1:3]) 
print(countries[1:6:2])
print(countries[-1:0:-1]) #end to start 


#overwritting the list elements
countries[0] = 'United States'
countries[3] = 'Canada'


#methods to apply to a list
print(len(countries))
print(type(countries)) #tipo de la estructura de datos
print(type(countries[-1]))


