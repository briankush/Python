student={'name':'Brian Kuria', 'age':'18'}
print(student)

student.update({'Residence':'Thika', 'Course':'Comp Sci', 'sport':'Table tennis'})
print(student)
print(len(student))
print(student.items())

for key,value in student.items():
    print(key.upper(),':', value.title())

Home=student.pop('Residence')
print(f'The student {student["name"]} resides in {Home}. He is {student["age"]}yrs old and currently learning {student['Course']}')    
del student['sport']
