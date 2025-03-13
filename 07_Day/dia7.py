# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Encuentra la longitud del conjunto it_companies
print(len(it_companies))
#Añadir 'Twitter' a it_companies
it_companies.add('Twitter')
print(it_companies)
#Insertar varias empresas de
#  TI a la vez en el conjunto it_companies
it_companies.update(['Instagram','Tesla'])
#Eliminar una de las empresas del conjunto it_companies
it_companies.remove('Tesla')
print(it_companies)
#¿Cuál es la diferencia entre eliminar y descartar?
#Si usando remove() el item no se encuentra en el set, arrojará error
#En cambio discard no arrojará nada

#Nivel 2
#Unir A y B
print(A.union(B))
#Encuentra A y B
print(A.intersection(B))
#Es un subconjunto de B
print(A.issubset(B))
#¿Son A y B conjuntos disjuntos?
print(A.isdisjoint(B))
#Join A with B and B with A
print(A.union(B))
print(B.union(A))
#What is the symmetric difference between A and B
print(A.symmetric_difference(B) )
#Delete the sets completely
del A

#Nivel 3
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ageS = set(age) 
print(age)
print(len(ageS))
print(len(age))
comp=len(ageS)== len(age)
print('El resultado de la comparación es: ',comp)
#Explain the difference between the following data types: string, list, tuple and set
#El tipo de dato String permite cualquier cadena de caracteres
#Los Sets no permiten datos repetidos
#En la tupla puedo añadir elementos, más no elimnarlos

#I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
set={'I','am','a','teacher','and', 'I ','love'}
set2={'to', 'inspire' ,'and','teach' ,'people'}
comp=set.symmetric_difference(set2)
print('Las palabras no repetidas son:',comp)

