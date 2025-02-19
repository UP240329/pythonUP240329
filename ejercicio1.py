
age=18
print(type(age))
height=75.5
print(type(height))
num=2j
print(type(num))
#4
base=float(input("Ingresa la medida de la base: "))
altura=float(input("Ingresa la altura del triángulo: "))
area=(base*altura)/2
print("El área del triángulo es: ",area)
#5
ladoA=float(input("Enter side a: "))
ladoB=float(input("Enter side b: "))
ladoC=float(input("Enter side c: "))
perimeter=ladoA+ladoB+ladoC
print("The perimeter of the triangle is: ",perimeter)
#6
length=float(input("Enter length of the rectangle: "))
width=float(input("Enter width of the rectangle: "))
area=length*width
perimeter=2*(length+width)
print("The perimeter of the triangle is: ",perimeter)
print("The perimeter and area of the triangle is: ",perimeter," , ",
area)
#7
radio=float(input("Enter radio of circle: "))
pi=3.14
area=pi*radio**2
circunference=2*pi*radio
print("The area of circle is: ",area)
print("The circunference of circle is: ",circunference)
#8
pendiente=2#Definición de la pendiente
interseccionY=-2
interseccionX=interseccionY/pendiente
print("La pendiente de la recta es: ",pendiente, "\nLa intersección con el eje X es en: ",interseccionX,"\nLa intersección con el eje Y es: ")
#9 Slope is (m = y2-y1/x2-x1). Find the slope 
# and Euclidean distance between point (2, 2) and point (6,10)
import math
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Slope: ",slope,"Distance: ", distance)
#10
print("Slopes are equal" if pendiente == slope else "Slopes are different")
#11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different 
# x values and figure out at what x value y is going to be 0.
x = int(input("Inserta el valor de x:"))
y = x**2 + 6*x + 9
print("El valor de y es: ", y)
#11.1
x = int(input("Inserta el valor de x: "))
y = x**2 + 6*x + 9
print("El valor de y es: ", y)
if y == 0:
    print("y es 0 cuando x es", x)
else:
    print("y no es 0 cuando x es", x)
#11.2
x = -3
y = x**2 + 6*x + 9
print("El valor de y es: ", y)  # This should print "El valor de y es:  0"
#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python')<len('dragon'))
#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')
#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'
print('jargon' in sentence)
#15 There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')
#16 Find the length of the text python and convert the value to float and convert it to string
print(str(float(len('python'))))
#17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num= int(input("Enter a number: "))
if num % 2 == 0:
    print(num," is an even number.")
else:
    print(num," is an odd number.")
#18 The floor division of 7 by 3 is equal to the int converted value of 2.7. make this statement true.
print(7//3 == int(2.7))
#19 Check if type of '10' is equal to 10
print(type('10')==type(10))
#20 Check if int('9.8') is equal to 10
print(int(float('9.8'))==10)
#21 Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours: "))     
rate = int(input("Enter rate per hour: "))
pay = hours * rate
print("Your weekly earning is: ", pay)
#22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60    
print("You have lived for ", seconds, " seconds.")
#23 Write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")




