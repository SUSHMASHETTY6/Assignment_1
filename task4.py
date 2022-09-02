
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print('Length of it_companies is: ', len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('Added Twitter to the set: ', it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Wipro', 'Infosys', 'Accenture'])
print('Added multiple companies: ', it_companies)

# Remove one of the companies from the set of it_companies
it_companies.remove('Accenture')
print('Removed Accenture from the set: ', it_companies)

# Difference between remove and discard
print("Difference remove and discard")
print("remove() method will raise an error if the  item is not present in the set,\n and the discard() method will not throw an error")

# Join A and B
A_B_union = A.union(B)
print('A join B is: ', A_B_union)

# Find A intersection B
A_B_intersection = A.intersection(B)
print('A and B intersection is: ', A_B_intersection)

# Find A subset of B
print('A is subset of B: ', A.issubset(B))

# Are A and B disjoint sets
print('A and B are disjoint sets: ', A.isdisjoint(B))

# Join B with A and A with B
A_join_B = A.union(B)
B_join_A = B.union(A)
print('A join B is: ', A_join_B)
print('B join A is: ', B_join_A)

# What is Symmetric difference between A and B
A_B_sym_diff = A.symmetric_difference(B)
print('Symmetric difference between A and B :', A_B_sym_diff)

# Delete the sets completely
A.clear()
B.clear()
print('Both the sets has been deleted')

# Convert the ages to a set and compare the length of the list and the set
age_set = set(age)
print('age set is: ', age_set)
if len(age) > len(age_set):
    print('Length of age which is of data type list is greater than length of age which is of data type set')
elif len(age_set) > len(age):
    print('Length of age which is of data type set is greater than length of age which is of data type list')
else:
    print('Both the lengths  are equal')