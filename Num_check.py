#This program sorts a list of numbers into odd or even numbers
numbers=[1,2,3,4,5,6,7,8,9,0]
odd_numbers=[]
even_numbers=[]

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f'The odd numbers are:\n{odd_numbers}')
print(f'The even numbers are:\n{even_numbers}')    
    