age=input('Please enter your age\n')
age=int(age)

while age:
    if age <0:
        print('Please enter a positive integer')
        break
    elif age <3:
        print('Your ticket is free')
        break
    elif age >=3 and age < 12:
        print('Your ticket price is $10')
        break
    else:
        print('Your ticket price is $15')
        break
        