classroom = [
    {
        "name": "Jane Doe",
        "grades": [
            {"grade": 90},
            {"grade": 80},
            {"grade": 100},
            {"grade": 70}
        ]
    },
    {
        "name": "Bob Ross",
        "grades": [
            {"grade": 100},
            {"grade": 90},
            {"grade": 70},
            {"grade": 60}
        ]
    },
    {
        "name": "John Doe",
        "grades": [
            {"grade": 50},
            {"grade": 90},
            {"grade": 90},
            {"grade": 85}
        ]
    },
    {
        "name": "John Smith",
        "grades": [
            {"grade": 90},
            {"grade": 80},
            {"grade": 90},
            {"grade": 90}
        ]
    },
    {
        "name": "Betty Smith",
        "grades": [
            {"grade": 100},
            {"grade": 85},
            {"grade": 100},
            {"grade": 100}
        ]
    },
    {
        "name": "Janet Hallow",
        "grades": [
            {"grade": 70},
            {"grade": 70},
            {"grade": 70},
            {"grade": 75}
        ]
    }
]
print(classroom)
print(classroom[1])
print(classroom[1]['name'])
print(classroom[1]['grades'])
print(classroom[1]['grades'][1])
print(classroom[1]['grades'][1]['grade'])

for student in classroom:
    print(f"{student['name']}")
    for grade in student['grades']:
        print(f"{grade['grade']}") 