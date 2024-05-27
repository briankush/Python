cubes=[number**3 for number in range (1,11)]
#for number in range(1,11):
    #cubes.append(number**3)
print(cubes)
print(f'The cubes of numbers between 1 and 10 are {cubes} and their sum is {sum(cubes)}')
odd_numbers=list(range(1,21,2))
for value in odd_numbers:
    print(value)
#print(f'The odd numbers between 1 and 20 are {odd_numbers}')
even_numbers=list(range(2,21,2))
print(f'The even numbers between 1 and 20 are {even_numbers}')
counting=list(range(1,1000001))
print(max(counting))
print(min(counting))
print(sum(counting))
