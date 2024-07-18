name= input('Please enter your name below \n')
def greet_user(name):
    #Docstring
    '''Display simple greating.'''
    print(f'Hello {name.title()}, how do you do?')

greet_user(name)

    
#Positional arguments
def means_of_transport(name, type):
    '''Displays information about my means of transport '''
    print(f'\nI have a {name}')
    print(f"My {name}'s type is {type} " )
   
means_of_transport('Motor cycle', 'Kawasaki ninja h2r') 
means_of_transport('Car', 'BMW')


#Keyword arguments
def describe_pet(animal_type='hamster', pet_name='harry'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()

#Default values
def describe_pet(pet_name, animal_type='dog'):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")
 
describe_pet('willie')
