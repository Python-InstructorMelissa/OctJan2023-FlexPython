park = [
    {
        "id": 1,
        "name": "Bronx Zoo",
        "location": "Bronx, NY",
        "animals": [
            {
                "id": 4,
                "name": "Lily Bee",
                "species": "Insect",
                "color": [
                    "Yellow",
                    "Black"
                ],
                "appendages": 6,
                "willToLive": True,
                "isDead": False,
                "health": 100,
            },
            {
                "id": 5,
                "name": "Jason Panda",
                "species": "Mammal",
                "color": [
                    "White",
                    "Black"
                ],
                "appendages": 4,
                "willToLive": True,
                "isDead": False,
                "health": 50,
            },
        ]
    },
    {
        "id": 2,
        "name": "San Francisco Zoo",
        "location": "San Francisco, CA",
        "animals": [
            {
                "id": 2,
                "name": "Donna Lady Bug",
                "species": "Insect",
                "color": [
                    "Red",
                    "Black"
                ],
                "appendages": 6,
                "willToLive": True,
                "isDead": False,
                "health": 100,
            },
            {
                "id": 3,
                "name": "Buzzy Bear",
                "species": "Mammal",
                "color": [
                    "Brown"
                ],
                "appendages": 4,
                "willToLive": True,
                "isDead": False,
                "health": 100,
            },
        ]
    },
    {
        "id": 3,
        "name": "Ninja Preserves",
        "location": "NinjaVille, Online",
        "animals": [
            {
                "id": 1,
                "name": "Carl Koala",
                "species": "Mammal",
                "color": [
                    "Grey"
                ],
                "appendages": 4,
                "willToLive": True,
                "isDead": False,
                "health": 60,
            },
            {
                "id": 6,
                "name": "Marvin Monkey",
                "species": "Mammal",
                "color": [
                    "Brown"
                ],
                "appendages": 4,
                "willToLive": True,
                "isDead": False,
                "health": 100,
            },
        ]
    }
]

# Reminders
# [] call the item by it's index - [0] or [i]
# {} call the item by it's key - ['keyName']

# Breakdown of how to pull something from each layer
# print(park)  # Whole list
# print(park[0])  # a park
# print(park[0]['name'])  # the park name
# print(park[0]['animals'])  # the parks list of animals
# print(park[0]['animals'][0])  # a animal
# print(park[0]['animals'][0]['name'])  # the animal's name
# print(park[0]['animals'][0]['color'])  # the animals list of colors
# print(park[0]['animals'][0]['color'][0])  # a color for the animal



# print all animals that have 4 appendages from 1 location
park01 = park[0]['animals']
for x in park01:
    # print(x['appendages'])
    if x['appendages'] == 4:
        print("4 appendages from 1 park",x['name'])

# print all animals that have 4 appendages regardless of location
for p in park:
    # print(p)
    for a in p['animals']:
        if a['appendages'] == 4:
            print("4 appendages from all parks",a['name'])

def appendages(legs):
    for p in park:
        for a in p['animals']:
            if a['appendages'] < legs:
                print(f'animal that has less than {legs} appendages: {a["name"]}')
                return a['name']
appendages(5)
appendages(9)

# print all animals who's health is less than 100 from 1 location
park01 = park[0]['animals']
for x in park01:
    if x['health'] < 100:
        print("less than perfect health 1 park",x['name'])

# print all animals who's health is less than 100 regardless of location
for p in park:
    for a in p['animals']:
        if a['health'] < 100:
            print("less than perfect health all parks",a['name'])

# print all the animal names from 1 location
park01 = park[0]['animals']
for x in park01:
    print("all animal names at 1 park", x['name'])

# print all the animals names regardless of location
for p in park:
    for a in p['animals']:
        print("all animal names at all parks", a['name'])

# print all the animals names if they have more than 4 appendages
for p in park:
    for a in p['animals']:
        if a['appendages'] > 4:
            print("all animal names at all parks with more than 4 appendages", a['name'])

# print all the different colors from all the animals but only list each color once
colors = []
for p in park:
    for a in p['animals']:
        for c in a['color']:
            print('all colors', c)
            if c not in colors:
                colors.append(c)
print("color list with no repeats", colors)