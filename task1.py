
import statistics
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort(reverse=False) # ascending to descending
print('After sorting the ages are as follows:', ages)

print('The min age is:', min(ages)) # min ages
print('The max age is:',max(ages)) # max ages

# Add the min age and the max age again to the list
ages.append(19) # add's 19(min) to list
ages.append(26) # add's 26(max) to list
ages.sort(reverse=False) # sorting again
print('After adding the ages of min and max,the new list is :',ages) #final sort

# Find the median age(one middle item or two middle items divided by two)
median = statistics.median(ages) # median
print('The median is :', median)

# Find the average age(sum of all items divided by their number)
mean = statistics.mean(ages) # mean
print('The mean is:', mean)

# Find the range of the ages (max minus min)
range = ages[len(ages)-1] - ages[0]
print('The range is :',range)
