#Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive.
#  If below 18 give feedback to wait for the missing amount of years. Output:
age=int(input('Enter your age: '))
if age >=18:
    print('You are old enough to drive')
else:
    print('You need to wait {18-age} years to drive')
#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) 
# to get the age as input. You can use a nested condition to print 'year'
#  for 1 year difference in age, 'years' for bigger differences, 
# and a custom text if my_age = your_age. Output:
my_age=18
your_age=int(input('Enter your age: '))
if my_age>your_age:
    print('I am older than you')
elif my_age<your_age:
    print('You are older than me')
else:
    print('We are the same age')
#Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
n1=int(input('Enter a number: '))
n2=int(input('Enter another number: '))
if n1>n2:
    print(n1,'is greater than ',n2)
elif n1<n2:
    print(n1,' is smaller than',n2)
else:
    print(n1,' is equal to', n2)
 #Nivel 2
 #