#Declare la función add_two_numbers . Esta función acepta dos parámetros y devuelve una suma.
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers()) 
#El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule área_del_círculo .
def areaCirculo():
    r=3
    pi=3.1416
    a=pi*r**2
    return a
print(areaCirculo())
#Escriba una función llamada add_all_nums que tome cualquier número de argumentos y los sume. Compruebe si todos los elementos de la lista son de tipo numérico. De no ser así, proporcione una respuesta razonable.
def add_all_nums(num):
    suma=0
    for num in num:    
        if type(num)==int or type(num)==float:
            suma=suma+num
            return suma
        else:
            print('No es un número')
print(add_all_nums(num=[1,2,3,4,5]))
#La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escriba una función que convierta °C a °F, convert_celsius_to-fahrenheit .
def convertCelsisuAFahrenheit(c):
    temperatura=(c*9/5)+32
    return temperatura
print(convertCelsisuAFahrenheit(c=30))
#Escriba una función llamada check-season, toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano.
def checkSeason(mes):
    if mes in ['Enero','Febrero','Marzo']:
        return 'Invierno'
    elif mes in ['Abril','Mayo','Junio']:
        return 'Primavera'
    elif mes in ['Julio','Agosto','Septiembre']:
        return 'Verano'
    else:
        return 'Otoño'
print(checkSeason(mes='Enero'))
#Escriba una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal
def calculateSlope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)
print(calculateSlope(x1=2,y1=2,x2=4,y2=4))
#La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. Escriba una función que calcule el conjunto solución de una ecuación cuadrática, solve_quadratic_eqn .
def solveQuadraticEqn(a,b,c):
    d=b**2-4*a*c
    if d>0:
        x1=(-b+d**0.5)/(2*a)
        x2=(-b-d**0.5)/(2*a)
        return x1,x2
    elif d==0:
        x=-b/(2*a)
        return x
    else:
        return 'No hay solución'
print(solveQuadraticEqn(a=1,b=5,c=6))
#Declara una función llamada print_list. Esta toma una lista como parámetro e imprime cada elemento de la lista.
def print_list(lista):
    for elemento in lista:
        print(elemento)
print_list(lista=[1,2,3,4,5])
#Declare una función llamada reverse_list. Esta recibe un array como parámetro y devuelve su valor inverso (usando bucles).
#print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
#print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
def reverse_list(lista):
    listaInversa=[]
    for i in range(len(lista)-1,-1,-1):
        listaInversa.append(lista[i])
    return listaInversa
print(reverse_list(lista=[1,2,3,4,5]))
#Declare una función llamada capitalize_list_items. Esta toma una lista como parámetro y devuelve una lista de elementos en mayúsculas
def capitalizeListItems(lista):
    listaMayusculas=[]
    for elemento in lista:
        listaMayusculas.append(elemento.upper())
    return listaMayusculas
print(capitalizeListItems(lista=['a','b','c','d','e']))
#Declara una función llamada add_item. Esta toma como parámetros una lista y un elemento. Devuelve una lista con el elemento añadido al final.
foodStaff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
def addItem(lista,elemento):
    lista.append(elemento)
    return lista
print(addItem(foodStaff,'Meat'))
print(addItem(numbers, 5))      
#Declara una función llamada remove_item. Esta toma como parámetros una lista y un elemento. Devuelve una lista con el elemento eliminado.
def removeItem(lista,elemento):
    lista.remove(elemento)
    return lista
print(removeItem(foodStaff,'Mango'))
#Declara una función llamada suma_de_números. Esta función toma un parámetro numérico y suma todos los números en ese rango.
def sumaNumeros(num):
    suma=0
    for i in range(1,num+1):
        suma=suma+i
    return suma
print(sumaNumeros(num=5))
#Declara una función llamada suma_de_impares. Esta función toma un parámetro numérico y suma todos los números impares en ese rango.
def sumaImpares(num):
    suma=0
    for i in range(1,num+1,2):
        suma=suma+i
    return suma
print(sumaImpares(num=5))
#Declara una función llamada suma_de_números_pares. Esta función toma un parámetro numérico y suma todos los números pares en ese rango.
def sumaPares(num):
    suma=0
    for i in range(0,num+1,2):
        suma=suma+i
    return suma
print(sumaPares(num=5))
#Nivel2
#Declare una función llamada evens_and_odds. Esta función toma un entero positivo como parámetro y cuenta el número de pares e impares en el número.
def evensAndOdds(num):
    par=0
    impar=0
    for i in range(1,num+1):
        if i%2==0:
            par=par+1
        else:
            impar=impar+1
    return par,impar
print(evensAndOdds(num=100))
#Llama a tu función factorial, toma un número entero como parámetro y devuelve un factorial del número.
def factorial(num):
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    return factorial
print(factorial(num=5))
#Llama a tu función is_empty , toma un parámetro y verifica si está vacío o no
def isEmpty(parametro):
    if len(parametro)==0:
        return True
    else:
        return False
print(isEmpty(parametro=[]))
#Escriba diferentes funciones que acepten listas.
# Estas funciones deben calcular la media, la mediana, la moda, el rango, la varianza y la desviación estándar (desviación estándar).
def media(lista):
    return sum(lista)/len(lista)
print(media(lista=[1,2,3,4,5]))
#Nivel 3
#Escriba una función llamada is_prime, que verifique si un número es primo.
def isPrime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True 
print(isPrime(num=7))       
#Escriba una función que verifique si todos los elementos son únicos en la lista.
def uniqueList(lista):
    for i in lista:
        if lista.count(i)>1:
            return False
    return True
print(uniqueList(lista=[1,2,3,4,5,5]))
#Escriba una función que verifique si todos los elementos de la lista son del mismo tipo de datos.
def sameType(lista):
    tipo=type(lista[0])
    for i in lista:
        if type(i)!=tipo:
            return False
    return True
print(sameType(lista=[1,2,3,4,5]))
#Escriba una función que verifique si la variable proporcionada es una variable de Python válida
def isPythonVariable(variable):
    if variable.isidentifier():
        return True
    else:
        return False
print(isPythonVariable(variable='variable1'))
#Vaya a la carpeta de datos y acceda al archivo Countries-data.py.
#Crea una función llamada "los idiomas más hablados del mundo". Debería devolver los 10 o 20 idiomas más hablados del mundo en orden descendente.
import countriesData as datac 
datos = datac.countries
countrylanguage = []

def idiomasMasHablados():
    for pais in datos:
        for lenguaje in pais['languages']:
            countrylanguage.append(lenguaje)
            
    setlanguages = set(countrylanguage)
    dictlanguages = {
    }
    for language in setlanguages:
        dictlanguages[language] = 0

    for idioma in dictlanguages:
        for pais in datos:  
             if idioma in pais['languages']:
                 dictlanguages[idioma] = pais['population'] + dictlanguages[idioma]

    sortValuesLanguagespopulation = sorted(dictlanguages.values(), reverse= True)
    sorfkeyslanguagespopulation = sorted(dictlanguages, key= dictlanguages.get, reverse=True)

    return sorfkeyslanguagespopulation[:10],sortValuesLanguagespopulation[:10]
print(idiomasMasHablados()) 
#Crea una función llamada "los países más poblados". Debería devolver los 10 o 20 países más poblados en orden descendente.
def paisesMasPoblados():
    dictPoblacion = {
    }
    for pais in datos:
        dictPoblacion[pais['name']] = pais['population']
    
    sortValuesPopulation = sorted(dictPoblacion.values(), reverse= True)
    sorfkeysPopulation = sorted(dictPoblacion, key= dictPoblacion.get, reverse=True)

    return sorfkeysPopulation[:10],sortValuesPopulation[:10]
print(paisesMasPoblados())

print("revisado")