# Task 9
no_of_students = int(input("Enter the number of students"))
wts = []
for i in range(no_of_students):
    txt = "Enter the " + str(i) + "th weights(lbs)"
    wts.append(float(input(txt)))
kgs = []
for wt in wts:
    kgs.append(wt * 0.453592) # Conversion factor
print(kgs)

