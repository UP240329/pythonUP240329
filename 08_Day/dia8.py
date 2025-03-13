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
    'Skills':['Weight lifting', 'hacer enojar a Javier'],
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
print(students['Skills'])
