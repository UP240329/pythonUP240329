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

#Nivel2
#Unir A y B
print(A.union(B))
#Encuentra A y B
print(A.intersection(B))
#Es un subconjunto de B
print(A.issubset(B))
#¿Son A y B conjuntos disjuntos?
print(A.isdisjoint(B))


