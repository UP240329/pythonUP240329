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
print("Slopes are equal" if m == slope else "Slopes are different")
#11

#12
print(len('python')>len('dragon'))
#13

