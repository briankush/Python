# TODO
print('''Please choose the Burgger that you want:
   Price List:

Mini Burger (M) : $5

Normal Burger (N): $8

Large Burger (L) : $10

Add Mushroom : For Mini and Normal = $1, For Large = $2

Extra Cheese : $1 ''')
size= input("Select the size you want ie M, N or L\n")
add_mushroom= input('''Wanna add some Mushroom?
For Mini and Normal = $1, For Large = $2. Reply with Y for yes or N for no\n''')
extra_cheese= input("And how about some extra Cheese for $1?\n")
bill=0
if(size=='M'):
    if(add_mushroom=="Y" and extra_cheese=='Y'):
        bill= 7
    elif(add_mushroom=="Y" and extra_cheese=='N' or add_mushroom=="N" and extra_cheese=='Y'):
        bill= 6
    else:
        bill= 5
if(size=='N'):
    if(add_mushroom=="Y" and extra_cheese=='Y'):
        bill= 10
    elif(add_mushroom=="Y" and extra_cheese=='N' or add_mushroom=="N" and extra_cheese=='Y'):
        bill= 9
    else:
        bill= 8
if(size=='L'):
    if(add_mushroom=="Y" and extra_cheese=='Y'):
        bill= 12
    elif(add_mushroom=="Y" and extra_cheese=='N' or add_mushroom=="N" and extra_cheese=='Y'):
        bill= 11
    else:
        bill= 10
print(f'''Your total bill amount is ${bill}. 
Thankyou for shopping with us''')
    
    
