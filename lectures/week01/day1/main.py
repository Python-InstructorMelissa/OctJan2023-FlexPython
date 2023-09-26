print("Hello World")


# Data Types and variables
x = "I am a string"
y = 24
z = True

x = 1000


# Tuples
iAmATuple = (24, "Favorite Number", True)
print(iAmATuple[1])

# iAmATuple[1] = "Testing"


# Lists
iAmList = ['Age', "Old As Dirt", 'Joking', 24, True]
print(iAmList[2])
iAmList[2] = "Not Joking"
iAmList.append("Halloween Baby") # .append will always add to the end of the list
iAmList.append("Joking")
iAmList.pop() # .pop will always remove the last item from the list
iAmList.insert(2, "Hey there everyone") # inserts what we want into the index that we specify
iAmList.remove("Old As Dirt") # simply removed the item we tell it to remove
# iAmList.remove("Old As Dirt")


# Dictionaries

# Reminders
# [] call the item by it's index - [0] or [i]
# {} call the item by it's key - ['keyName']

cohort = {"students": "many", "subject": "Python", "location": "Online"}
print(cohort['subject'])

theSubject = cohort['subject']
theLocation = cohort['location']
theStudents = cohort['students']

print("printing info from cohort:", theSubject, theLocation, theStudents)
print("printing info from cohort:"+ theStudents+theLocation+theSubject)
print("Melissa's class is held {} and is teaching {}.  She has {} students".format( theLocation, theSubject, theStudents))
print(f"Melissa's class is held {theLocation}, and is teaching {theSubject}. She has {theStudents} Students")

x = 10
# x = 5
# x = 6
if (x < 5):
    print(x)
    print(True)
else:
    print(False)

y = 9

if (y < 10):
    print("y is less than 10") #if true print me
elif (y < 5):
    print("y is less than 5") # if above is false but i am true print me
else:
    print("no if statement was true") # if none are true then print me


for i in iAmList:
    print(i)

for i in range(0, 4):
    print(i)
    print()