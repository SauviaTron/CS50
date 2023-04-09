peoples = [
    {"name": "Harry", "house": "Gryfffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["name"]

# peoples.sort(key=f)
peoples.sort(key=lambda person: person["name"])

print(peoples)