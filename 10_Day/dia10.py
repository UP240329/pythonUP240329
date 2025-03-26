#Iterate 0 to 10 using for loop, do the same using while loop.
count=0
while count<= 10:
    print(count)
    count=count+1
numbers=[1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)
#Itere de 10 a 0 usando el bucle for, haga lo mismo usando el bucle while.
count=10
while count>=1:
    print(count)
    count=count-1
numbers=[10,9,8,7,6,5,4,3,2,1]
for number in numbers:
    print(number)
# Escriba un bucle que realice siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:
  #
  ##
  ###
  ####
  #####
  ######
  #######
for i in range(8):
    print("#"*i)
#Utilice bucles anidados para crear lo siguiente:
sq=1
for c in range(8):
   print(sq*8)

m=3
n=4
for j in range(m):
    for i in range(n):
        print("# ")
#Imprima el siguiente patrón:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100
for i in range(11):
    print(i,"x",i,"=",i*i)
#Itere a través de la lista, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] usando un bucle for e imprima los elementos.
lenguajes=['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for lenguaje in lenguajes:
    print(lenguaje)
#Utilice el bucle for para iterar de 0 a 100 e imprimir solo números pares
for i in range(0,101,2):
    print(i)
#Utilice el bucle for para iterar de 0 a 100 e imprimir solo números impares
for i in range(1,100,2):
    print(i)
#Nivel2
#Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los números.
suma=0
for n in range(101):
    suma=suma+n
print('El totral de la suma es de ',suma)
#Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los pares y la suma de todos los impares.
#The sum of all evens is 2550. And the sum of all odds is 2500.
sumaPar=0
sumaImpar=0
for n in range(101):
    if n%2==0:
        sumaPar=sumaPar+n
    else:
        sumaImpar=sumaImpar+n
print('La suma de todos los pares es de ',sumaPar,'. Y la suma de todos los impares es de ',sumaImpar)
#Nivel3
#Vaya a la carpeta de datos y utilice el archivo Countries_data.py
import countriesData as datac 

datos = datac.countries
countrylanguage = []
for pais in datos:
    for lenguaje in pais['languages']:
        countrylanguage.append(lenguaje)
        
print('La cantidades de lenguajes en countriesdata son: ', len(countrylanguage))

#Encuentre los diez idiomas más hablados a partir de los datos

setlanguages = set(countrylanguage)
dictlanguages = {

}
for language in setlanguages:
    dictlanguages[language] = 0

print(dictlanguages)

for idioma in dictlanguages:
    for pais in datos:  
         if idioma in pais['languages']:
             dictlanguages[idioma] = pais['population'] + dictlanguages[idioma]

sortValuesLanguagespopulation = sorted(dictlanguages.values(), reverse= True)
sorfkeyslanguagespopulation = sorted(dictlanguages, key= dictlanguages.get, reverse=True)

print( sorfkeyslanguagespopulation[1] ,sortValuesLanguagespopulation[1])

#Encuentra los 10 países más poblados del mundo
print('Los 10 idiomas mas hablados en el mundo son (orden decendente)')
for i in range(10):
    print(sorfkeyslanguagespopulation[i] ,sortValuesLanguagespopulation[i])