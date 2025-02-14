age=18
print(type(age))
height=75.5
print(type(height))
num=2j
print(type(num))

base=float(input("Ingresa la medida de la base: "))
altura=float(input("Ingresa la altura del triángulo: "))
area=(base*altura)/2
print("El área del triángulo es: ",area)

ladoA=float(input("Enter side a: "))
ladoB=float(input("Enter side b: "))
ladoC=float(input("Enter side c: "))
perimeter=ladoA+ladoB+ladoC
print("The perimeter of the triangle is: ",perimeter)

length=float(input("Enter length of the rectangle: "))
width=float(input("Enter width of the rectangle: "))
area=length*width
perimeter=2*(length+width)
print("The perimeter of the triangle is: ")
print("The perimeter and area of the triangle is: ",perimeter," , "+area)