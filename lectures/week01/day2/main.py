#  print the numbers 1-10

# for loop to go through 1-10
def numoneTen():
    for x in range(1, 11):
        print(x)

# numoneTen()


# print the even numbers 1-10

# for loop go through 1-10
# conditional to check for even

def evens():
    for x in range(1, 11):
        if (x % 2 == 0):
            print(x)

# evens()

testing = [1,2,3,4]

for x in testing:
    if 5 not in testing:
        # print("nope")
        pass


# Use the following dictionary for the next few
users = [
    {
        "firstName": "Melissa",
        "lastName": "Longenberger",
        "progLang": [
            "JS",
            "Python",
            "C#", 
            "Java"
        ]
    },
    {
        "firstName": "Edmund",
        "lastName": "Periwinkle",
        "progLang": [
            "HTML",
            "CSS"
        ]
    },
    {
        "firstName": "Bob",
        "lastName": "Ross",
        "progLang": [
            "HTML",
            "CSS",
            "LESS"
        ]
    },
    {
        "firstName": "Jane",
        "lastName": "Doe",
        "progLang": [
            "Java",
            "Vite",
            "React"
        ]
    }
]
# Testing / Examples

# Reminders
# [] call the item by it's index - [0] or [i]
# {} call the item by it's key - ['keyName']


# print(users) # The whole list
# print(users[1]) # 1 Dict from main list
# print(users[1]['firstName']) # 1 key/value from dict in list
# print(users[1]['progLang']) # 1 key/value/list form dict in list
# print(users[1]['progLang'][1]) # 1 index in list in dict in list


for user in users:
    # print(user)
    # print(user['firstName'])
    pass


# print the first names in the dictionary
for user in users:
    # print(user)
    # print(user['firstName'])
    pass

# print the first names and last names in this dictionary  - like this lastName, firstName
for user in users:
    # print(user['lastName']+ ", " + user['firstName'])
    # print(f"{user['lastName']}, {user['firstName']}")
    pass

# print the first name and then the list of programming languages that each user has
for user in users:
    print(f"{user['firstName']}, {user['progLang']}")


for user in users: # for index in users list
    print(f"{user['firstName']}:") # index['keyname']
    for l in user['progLang']: # for index in each user
        print(f"{l}") # value at index