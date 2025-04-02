#Filtrar solo los negativos y ceros en la lista usando la comprensión de listas
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_even_numbers = [i for i in numbers if i <=0]
print(positive_even_numbers)  
#Aplana la siguiente lista de listas de listas a una lista unidimensional:
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for number in list_of_lists for sublist in number for number in sublist]
print(flattened_list)
#Usando la comprensión de listas, cree la siguiente lista de tuplas:
tuplas = [(i, *[i**j for j in range(7)]) for i in range(11)]
print(tuplas)
#Aplana la siguiente lista a una nueva lista: countries =
#output:
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lista=[i for i in countries for sublist in i for i in sublist]
lista=[[i.upper()] for i in lista]
print(lista)
#Cambie la siguiente lista a una lista de diccionarios:
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]
paises = [{'country': i[0].upper(), 'city': i[1].upper()} for sublist in paises for i in sublist]
print(paises)
#Cambie la siguiente lista de listas a una lista de cadenas concatenadas:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output:
#['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [' '.join(i) for sublist in names for i in sublist]
print(names)
#Escriba una función lambda que pueda resolver una pendiente o una intersección con el eje y de funciones lineales
def slope_intercept(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    y_intercept = y1 - slope * x1
    return slope, y_intercept
print(slope_intercept(1, 2, 3, 4))

