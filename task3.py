"""Create a tuple containing names of your sisters and your brothers (imaginary siblings are
fine)"""

sisters = ('sana', 'priya', 'siri', 'sweety') # tuple for sisters
brothers = ('john', 'james', 'jones') # tuple for brothers

# Join brothers and sisters tuples and assign it to siblings
sibilings = sisters + brothers # sisters and brothers-- siblings
print('Brothers are: ', brothers)
print('Sisters are: ', sisters)
print('Siblings are: ', sibilings)

# How many siblings do you have
print('Number of sibilings are: ', len(sibilings)) # count of siblings

modified_sibilings = list(sibilings) #modifying siblings list
father='steves'
mother='sam'
print('father name is:', father)
print('mother name is:', mother)

father=modified_sibilings.append('Steves') # adding father to family_members
mother=modified_sibilings.append('Sam') # adding mother to family_members

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = tuple(modified_sibilings) # new list
print('Family members: ', family_members) # prints all family_memebers