#Declare la función add_two_numbers . Esta función acepta dos parámetros y devuelve una suma.
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
#El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule área_del_círculo .
def areaCirculo(r):
    return 3.1416*r*r
#Escriba una función llamada add_all_nums que tome cualquier número de argumentos y los sume. Compruebe si todos los elementos de la lista son de tipo numérico. De no ser así, proporcione una respuesta razonable.
def addNums(*args):
    suma=0
    for n in args:
        if type(n)==int or type(n)==float:
            suma=suma+n
        else:
            return print('No todos los elementos son numéricos')
        print(suma)
#La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escriba una función que convierta °C a °F, convert_celsius_to-fahrenheit .
def convertCelsisuAFahrenheit(c):
    return (c*9/5)+32
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
#Escriba una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal
def calculateSlope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)
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
#Declara una función llamada print_list. Esta toma una lista como parámetro e imprime cada elemento de la lista.
def print_list(lista):
    for elemento in lista:
        print(elemento)
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


