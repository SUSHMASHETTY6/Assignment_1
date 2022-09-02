import statistics
# Create an empty dictionary called dog
my_new_dict = {}

print("Dog:",my_new_dict)

# Add name, color, breed, legs, age to the dog dictionary
Dog = {
    'Dog_name':'Kittu',
    'color':'Brown',
    'breed':'shihtzu',
    'age':'6 months',
    'legs':'4 (short)',
        }
print('The Dog dictionary is:\n',Dog)

"""Create a student dictionary and add first_name, last_name, gender, age, marital status,
skills, country, city and address as keys for the dictionary """
Student = {
    'first_name':'Shreya',
    'last_name':'saran',
    'gender':'female',
    'age':23,
    'marital status':'single',
    'skills':['JavaScript','SAP','php','C#','Python'],
    'Country':'United States',
    'address':{
        'street':'Rosery street',
        'zipcode':'66123'
    }
    }
print('The Student dictionary is:\n',Student)
x=[]
x=Student["skills"]

# Get the length of the student dictionar
print('The length of Student dictionary is:',len(Student))

# Get the value of skills and check the data type, it should be a list
print("Data type of skills is : {} \n ".format(type(x)))

# Modify the skills values by adding one or two skills
Student['skills'].append('HTML')
Student['skills'].append('CSS')
print("The updated skills :{} \n".format(Student["skills"]))

# Get the dictionary keys as a list
Dog_keys=list(Dog.keys())
print("The keys are of dog dictionary are : {} \n".format(Dog_keys))

# Get the dictionary values as a list
Student=list(Student.values())
print("The values of student dictionary are : {} \n".format(Student))
