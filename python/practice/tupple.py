info = [
    ("meet", "science"),
    ("mitul", "math"),
    ("mitul", "english"),
    ("mitul", "spot"),
    ("hiren", "english"),
    ("hiren", "hindi"),
    ("darshn", "eco"),
    ("anjli", "hindi"),
    ("vasu", "spot")
]

# unique names
unique_name = set()
for tup in info:
    for item in tup:
        unique_name.add(item)
        print(item)
print(unique_name)

# create a dictionary

dict = {}
for name, course in info:
    if (dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)
