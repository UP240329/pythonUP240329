import functools
from functools import reduce
#Explique la diferencia entre mapa, filtro y reducción.
#map aplica una función a cada elemento de una lista y devuelve una nueva lista con los resultados.
#filter aplica una función a cada elemento de una lista y devuelve una nueva lista con los elementos que cumplen la condición.
#reduce aplica una función a los elementos de una lista y devuelve un solo valor acumulado.
#########
#Explique la diferencia entre función de orden superior, cierre y decorador.
#Una función de orden superior es una función que toma otra función como argumento o devuelve una función como resultado.
#Un cierre es una función que recuerda el entorno en el que fue creada, incluso si se ejecuta fuera de ese entorno. 
#Un decorador es una función que toma otra función y extiende su comportamiento sin modificarla directamente.
#########
#Defina una función de llamada antes de map, filter o reduce, vea los ejemplos a continuación.
numbers = [1, 2, 3, 4, 5]  
numbers_str = ['1', '2', '3', '4', '5']  
numbers_int = map(int, numbers_str)
print(list(numbers_int)) 

def is_even(num):
    if num % 2 == 0:
        return True
    return False
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  

numbers_str = ['1', '2', '3', '4', '5']  
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)  

#Utilice el bucle for para imprimir cada país en la lista de países.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)
#Utilice for para imprimir cada nombre en la lista de nombres.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)

#Utilice for para imprimir cada número en la lista de números.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

#Nivel2
#Utilice el mapa para crear una nueva lista cambiando cada país a mayúscula en la lista de países
def upper(countries):
    return countries.upper()
print(list(map(upper, countries))) 
#Utilice el mapa para crear una nueva lista cambiando cada número por su cuadrado en la lista de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(num):
    return num ** 2
print(list(map(square, numbers)))
#Utilice el mapa para cambiar cada nombre a mayúsculas en la lista de nombres
namesM=map(str,names)
namesM=[i.upper()for i in namesM]
print(list(namesM))
#Utilice el filtro para filtrar los países que contienen la palabra "tierra".
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def land(countries):
    if 'land' in countries:
        return True
    return False
print(list(filter(land, countries)))
#Utilice el filtro para filtrar países que tengan exactamente seis caracteres.
def six(countries):
    if len(countries) == 6:
        return True
    return False
print(list(filter(six, countries)))
#Utilice el filtro para filtrar los países que contengan seis letras o más en la lista de países.
def sixMas(countries):
    if len(countries) >= 6:
        return True
    return False
print(list(filter(sixMas, countries)))
#Utilice el filtro para filtrar los países que comienzan con 'E'
def paisesE(countries):
    if 'E' in countries[0]:
        return True
    return False
print(list(filter(paisesE, countries)))
#Encadenar dos o más iteradores de lista (por ejemplo, arr.map(callback).filter(callback).reduce(callback))
def multiplicar_por_dos(x):
    return x * 2

def es_par(x):
    return x % 2 == 0

def sumar(acc, x):
    return acc + x

arr = [1, 2, 3, 4, 5]
resultado = (
    reduce(
        sumar,  
        filter(
            es_par,  
            map(multiplicar_por_dos, arr)  
        )
    )
)
print(resultado)
#Declare una función llamada get_string_lists que toma una lista como parámetro y luego devuelve una lista que contiene solo elementos de cadena.
lst=['Monica',2,3,20,'Upa']
def string(lst):
    if type==str in lst:
        return True
    return False
print(list(filter(string, lst)))




