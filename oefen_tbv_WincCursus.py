'''
print('We have a long road ahead.')
for i in range(1000):
    if i % 2 == 0:
        print(i)
        continue
    print('Almost theree...')
print("That wasn't half bad.")
'''

students = [
    {
        "name": "Ali",
        "family_name": "Khan",
        "skills": {
            "Python": "beginner",
            "JavaScript": "expert",
        },
        "certificates": [
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Data Analytics with Python",
                "date_of_completion": "",
            },
        ],
    },
    {
        "name": "Jessica",
        "family_name": "van Alphen",
        "skills": {
            "Python": "advanced beginner",
            "JavaScript": "beginner",
        },
        "certificates": [
            {
                "name": "Front-end Development",
                "date_of_completion": "",
            },
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Data Analytics with Python",
                "date_of_completion": "2020-01-17",
            },
        ],
    },
]

print(students[1]["skills"]["Python"])  # "advanced beginner"
print(students[0]["certificates"][1]["name"])  # "Back-end Development"