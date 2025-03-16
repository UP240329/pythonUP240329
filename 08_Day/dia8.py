#Create an empty dictionary called dog
dog = {}
#Add name, color, breed, legs, age to the dog dictionary
dog['key1']='Javier'
dog['key2']='Negro'
dog['key3']='Pastor Alemán'
dog['key4']='4'
dog['key5']='2'
print(dog)
#Create a student dictionary and add first_name, last_name
#  gender, age, marital status, skills, country, city and address as keys for the dictionary
students={
    'Name':'Monica',
    'LastName':'Escobedo',
    'Gender':'Female',
    'Age':'18',
    'MaritalStatus':'Soltera',
    'Skills':['Weight lifting'],
    'Country':'México',
    'City':'Aguascalientes',
    'Address':{
        'Street':'Priv. Ave del Paraíso #226',
        'Localidad':'El llano Jesús María, Aguascalientes'
        }
}
#Get the length of the student dictionary
print(len(students))
#Get the value of skills and check the data type, it should be a list
skills=students['Skills']
print(skills)
print(type(skills))
#Modify the skills values by adding one or two skills
students['Skills'].append('Excel')
students['Skills'].append('Leer')
print(students)
#Get the dictionary keys as a list
keys = students.keys()
print(keys) 
#Get the dictionary values as a list
values = students.values()
print(values)   
#Change the dictionary to a list of tuples using items() method
print(students.items()) 
#Delete one of the items in the dictionary
students.pop('MaritalStatus')
print(students)
#Delete one of the dictionaries
del students
