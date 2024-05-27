first_name = ("brian ")
middle_name= 'kuria'
last_name = "mwangi"
full_name = f"{first_name} {middle_name} {last_name}"
message= f"Hello, {full_name.title()}!"
print(message)
first_name='albert'
print(message)
Languages=['Python', 'Java', 'C', 'Ada.']
famous_person= 'Albert Einstein'
new_message= '''\tonce said, A person who never made a 
mistake never tried anything new.'''
print(f"{famous_person.upper()}{new_message}")
print(Languages)
programming_languages=['Java script', 'C#', 'C++', ]
programming_languages.append('Ruby')
Languages.extend (programming_languages)
#print(Languages)
#Languages.pop(5)
#print(Languages)
for item in Languages:
    print(Languages)
    
guest_list=['Cecilia', 'Anderson','Florence','Brian','Albert']  
for guest in guest_list:
    message=f'''Hello dear {guest}. I hearby take this opportunity to welcome you
to my graduation ceremony that will take place at Machakos university on Teusday at 3pm. Your 
presence will be highly appreciated.'''
    print(message)
squares=[value**2 for value in range(1,11)]
#for value in range(1,11):
    #square=value**2
    #squares.append(square)
    #squares.append(value**2)
print(f'the squares are {squares}')
print(f'Their sum is {sum(squares)}')


