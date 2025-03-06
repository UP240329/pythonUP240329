#declare a empty list
emptylist=[]
#Declare a list with more than 5 items
lista=['Programación','Metrología','Alemán','Inglés','Procesos Industriales']
#Find the length of your list
print(len(lista))
#Get the first item, the middle item and the last item of the list
print(lista[0],lista[2],lista[4])
#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Monica',18,1.63,'Soltera','Priv. Ave del Paraiso 226']
#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
#Print the list using print()
print(it_companies)
#Print the number of companies in the list
print(len(it_companies))
#Print the first, middle and last company
print(it_companies[0],it_companies[3],it_companies[6])
#Print the list after modifying one of the companies
print(it_companies)
it_companies[0]='Instagram'
print(it_companies)
#Add an IT company to it_companies
print(it_companies)
it_companies.append('Microsoft')
#Insert an IT company in the middle of the companies list
print(it_companies)
it_companies.insert(3, 'Tesla')
#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1]=it_companies[1].upper()
print(it_companies)
#Join the it_companies with a string '#;  '
print('#'.join(it_companies))
#Check if a certain company exists in the it_companies list
does_exist = 'Tesla' in it_companies
print(does_exist)
#Sort the list using sort() method
it_companies.sort() 
print(it_companies)
#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
#Slice out the first 3 companies from the list
print(it_companies[3:9])
#Slice out the last 3 companies from the list
print(it_companies[1:6])
#Slice out the middle IT company or companies from the list
print(it_companies[1:5]+ it_companies[6:9])
#Remove the first IT company from the list
del it_companies[0]
print(it_companies)
#Remove the middle IT company or companies from the list
del it_companies[5]
print(it_companies)
#Remove the last IT company from the list
it_companies.pop()
print(it_companies)
#Remove all IT companies from the list
del it_companies

#Destroy the IT companies list
#it_companies.clear() 

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
lista=front_end+back_end
print(lista)
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack,
#  then insert Python and SQL after Redux.
listaCopy=lista.copy()
fullStack=listaCopy
print(fullStack)
fullStack.insert(5,'python')
fullStack.insert(6,'SQL')
print(fullStack)
#LEVEL TWO
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages.sort()
print(ages[0],ages[len(ages)-1])
#Add the min age and the max age again to the list
ages.insert(0,19)
ages.insert(-1,26)
print(ages)
# Find the median age (one middle item or two middle items divided by two)
mediana = (ages[4] + ages[5]) / 2
print("La mediana es: ", mediana)
#Find the average age (sum of all items divided by their number )
promedio = sum(ages) / len(ages)
print("El promedio es: ", promedio)
#Find the range of the ages (max minus min)
rango = ages[len(ages)-1] - ages[0]
print("El rango de las edades es: ",rango)
#Compare the value of (min - average) and (max - average), use abs() method
comp=(ages[0]-promedio)and (ages[-1]-promedio)
print("La comparación es: ", comp)
#Find the middle country(ies) in the countries list
import paises as p
paises=p.countries
print(len(paises))



