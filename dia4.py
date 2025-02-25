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

