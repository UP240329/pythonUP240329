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
def get_string_lists(lst):
    return [i for i in lst if isinstance(i, str)]
print(get_string_lists(lst))
#Utilice reducir para sumar todos los números en la lista de números.
numbers = [1, 2, 3, 4, 5]
def add(x, y):
    return x + y
total = reduce(add, numbers)
print(total)
#Utilice reduce para concatenar todos los países y producir esta oración:
#  Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa.
from functools import reduce
paises = ["Estonia", "Finlandia", "Suecia", "Dinamarca", "Noruega", "Islandia"]
def concatenar(x, y):
    return x + ", " + y
oracion = reduce(concatenar, paises)
oracionFinal = oracion + " son países del norte de Europa."
print(oracionFinal)
#Declare una función llamada categorize_countries que devuelva una lista de países con algún patrón común 
# (puede encontrar la lista de países en este repositorio como Countries.js (por ejemplo, 'land', 'ia', 'island', 'stan')).
from paises import countries  
def categorizeCountries(patterns):
    categorized = {}
    for pattern in patterns:
        categorized[pattern] = [country for country in countries if pattern in country]
    return categorized
patterns = ['land', 'ia', 'island', 'stan']
result = categorizeCountries(patterns)
print(result)
#Crea una función que devuelva un diccionario, donde las claves representan
#  las letras iniciales de los países y los valores son la cantidad de nombres de países que comienzan con esa letra.
from paises import countries
def countI():
    initialCount = {}
    for country in countries:
        initial = country[0].upper()
        if initial not in initialCount:
            initialCount[initial] = 1
        else:
            initialCount[initial] += 1
    return initialCount
initialCount = countI()
print(initialCount)
#Declare una función get_first_ten_countries: devuelve una lista de los primeros diez países de la lista Countries.js en la carpeta de datos.
def First():
    return countries[:10]
FirstTen = First()
print(FirstTen)
#Declare una función get_last_ten_countries que devuelva los últimos diez países de la lista de países.
def Last():
    return countries[-10:]
LastTen = Last()
print(LastTen)
#Nivel3
#Ordenar países por nombre, por capital, por población
import paises1 as paises  
def obtenerNombre(pais):
    return pais["name"]
def obtenerCapital(pais):
    return pais["capital"]
def obtenerPoblacion(pais):
    return pais["population"]
def ordenarPorNombre(paises):
    return sorted(paises, key=obtenerNombre)
def ordenarPorCapital(paises):
    return sorted(paises, key=obtenerCapital)
def ordenarPorPoblacion(paises, reverse=False):
    return sorted(paises, key=obtenerPoblacion, reverse=reverse)
paisesLista = paises.paises  
ordenadoPorNombre = ordenarPorNombre(paisesLista)
print("\nOrdenado por nombre:")
for pais in ordenadoPorNombre:
    print(pais["name"])
ordenadoPorCapital = ordenarPorCapital(paisesLista)
print("\nOrdenado por capital:")
for pais in ordenadoPorCapital:
    print(pais["capital"])
ordenadoPorPoblacion = ordenarPorPoblacion(paisesLista, reverse=True)
print("\nOrdenado por población (de mayor a menor):")
for pais in ordenadoPorPoblacion:
    print(f"{pais['name']} - {pais['population']}")

#Clasifique los diez idiomas más hablados por ubicación.
from collections import Counter
import paises1 as paises
def contarTop10Idiomas():
    idiomas = []
    for pais in paises.paises:  
        if "languages" in pais:  
            idiomas.extend(pais["languages"]) 
    top10Idiomas = Counter(idiomas).most_common(10)
    return top10Idiomas
def mostrarTop10Idiomas():
    top10Idiomas = contarTop10Idiomas()
    print("Los 10 idiomas más hablados globalmente son:")
    for idioma, count in top10Idiomas:
        print(f"{idioma}: {count}")
mostrarTop10Idiomas()
#Clasifique los diez países más poblados.
def clasificarPaisesMasPoblados():
    paisesOrdenados = sorted(paises.paises, key=lambda pais: pais["population"], reverse=True)
    return paisesOrdenados[:10]
def mostrarTop10PaisesMasPoblados():
    top10Paises = clasificarPaisesMasPoblados()
    print("Los 10 países más poblados son:")
    for pais in top10Paises:
        print(f"{pais['name']}: {pais['population']}")
mostrarTop10PaisesMasPoblados()

