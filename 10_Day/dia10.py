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
i=1
while i<=7:
    print("#"*i)
    i=i+1
for i in range(1,8):
    print("#"*i)
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

