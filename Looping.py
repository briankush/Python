number=0
while number <=5:
    print(number)
    number+=1
    
    
# Using continue in a loop

current_number = 0
while current_number < 10:
 current_number += 1
 if current_number % 2 == 0:
    continue
 
 print(f'\n {current_number}')

 # Using a flag  
prompt='''\n Tell me something and i will repeat it back to you:
 Enter 'quit' to end the program \n'''
active= True
while active: 
    message=""
    message=input(prompt)
    
    if message == 'quit':
        active= False
    else:
        print(message)


            
 