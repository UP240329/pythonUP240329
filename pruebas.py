company="Coding For All"
subString="C"
example="You cannot end a sentence with because because because is a conjunction"
print(example.rfind("because"))
example="You cannot end a sentence with because because because is a conjunction"
example=example.split()


example="You cannot end a sentence with because because because is a conjunction"
print(example.index("because"))
print(example.rindex('because'))
print(example[31:47])
print(company[6:14])
print(len(example))

subString="Coding"
print(subString + company)
print(company.index(subString))
print(subString in company)

print(company.endswith('coding'))
print(company.startswith(subString))