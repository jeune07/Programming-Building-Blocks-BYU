people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest=None
min_age=float("inf")


for person in people:
    name,age=person.split() 
    age=int(age)
    if age < min_age:
        min_age = age
        youngest=name
print(f"the younngest is {youngest} his age is {min_age}")


