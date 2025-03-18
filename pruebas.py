fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=str(input('Enter a fruit'))
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)
