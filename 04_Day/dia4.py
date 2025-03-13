#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first= 'thirty '
second='days '
third='of '
fourth='python'
print(first + second+ third + fourth)
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
first= 'Coding '
second='For '
third='All'
print(first + second+ third)
#Declare a variable named company and assign it to an initial value "Coding For All".
company="Coding For All"
#Print the variable company using print()
print(company)
#Print the length of the company string using len() method and print()
print(len(company))
#Change all the characters to uppercase characters and print()
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
#Cut(slice) out the first word of Coding For All and print()
print(company[6:14])
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))
print('Coding' in company)
#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))
#Change Python for Everyone to Python for All using the replace method or other methods.
companyy="Python for all"
print(companyy.replace('Python','Everyone'))
#Split the string 'Coding For All' using space as the separator (split()) 
print(company.split())
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
oracion="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(oracion.split(','))
#What is the character at index 0 in the string Coding For All.
print(company[0])
#What is the last index of the string Coding For All.
print(company[-1])
#What character is at index 10 in "Coding For All" string.
print(company[10])
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
name="Python For Everyone"
name=name.split()
print(name[0][0]+name[1][0]+name[2][0])
#Create an acronym or an abbreviation for the name 'Coding For All'.
name="Coding For All"
name=name.split()
print(name[0][0]+name[1][0]+name[2][0])
#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))
#Use index to determine the position of the first occurrence of F in Coding For All
print(company.index("F"))
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
oracion="Coding For All People"
print(oracion.rfind("l"))
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
#  'You cannot end a sentence with because because because is a conjunction'
example="You cannot end a sentence with because because because is a conjunction"
print(example.index("because"))
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 
print(example.rindex('because'))
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(example[0:30]+example[54:71])
#Does ''Coding For All' start with a substring Coding?
subString="Coding"
print(company.startswith(subString))
#Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
variable='   Coding For All   '
print(variable.strip())
#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
v1="30DaysOfPython"
v2="thirty_days_of_python"
print(v1.isidentifier())
print(v2.isidentifier())
#The following list contains the names of some of python libraries:
librerias=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(librerias))
#Use the new line escape sequence to separate the following sentences
print('I am enjoying this challenge''\n''I just wonder what is next')
#Use a tab escape sequence to write the following lines.
print('Name'+'\t'+'Age'+'\t'+'Country'+'\t''City')
print('Monica'+'\t'+'250'+'\t'+'Finland'+'\t''Helsinky')
#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
print('El área del circulo es: '+str(area))
print("8 + 6 = {}".format(8+6))
print("8 - 6 = {}".format(8-6))
print("8 * 6 ={}".format(8*6))
print("8 / 6 ={}".format(8/6))
print("8 % 6 = {}".format(8 % 6))
print("8//6={}".format(8//6) )
print("8 ** 6 = {}".format(8**6))




#REVISADO
print("Revisado")