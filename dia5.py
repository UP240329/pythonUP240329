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
#


