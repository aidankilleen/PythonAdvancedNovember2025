# sorting_investigation.py


from Person import Person


names = ["aidan", "tracy", "mary", "Zoe", "Yvonne", "Jack", "Alice", "Eve"]

# list .sort() method sorts the list in-place 
print (names)
names.sort()
print (names)

names.sort(reverse=True)

print (names)

def to_upper(name: str) -> str:
    return name.upper()

names.sort(key=to_upper)
print (names)

# use a lambda for the key function
names.sort(key=lambda name: name.upper(), reverse=True)
print (names)


people = [
    Person(11, "eve", "eve@gmail.com", True), 
    Person(9, "dan", "dan@gmail.com", False),
    Person(15, "Alice", "alice@gmail.com", True),
    Person(25, "zoe", "alice@gmail.com", True),
    Person(5, "Yvonne", "alice@gmail.com", True),
    Person(75, "Wendy", "alice@gmail.com", True),
    Person(2, "Carol", "carol@gmail.com", True),
    Person(12, "Bob", "bob@gmail.com", False)    
]

def get_sort_key(person):
    return person.name

people.sort(key=get_sort_key)
print (people)

people.sort(key=lambda person: person.id)
print (people)

print ("*" * 30)
# sorted
# 
print (names)

sorted_names = sorted(names)

print (sorted_names)
print (names)

sorted_names = sorted(names, key=lambda name:name.upper())
print (sorted_names)


sorted_people = sorted(people)

print (sorted_people)


sorted_by_name = sorted(people, key=lambda person:person.name.upper())

print (sorted_by_name)
print ("\n".join([person.name for person in sorted_by_name]))

active_people = [person for person in sorted_by_name if person.active]

print ("\n".join([person.name.title() for person in active_people]))


people_tuple = ("Zoe", "Yvonne", "Alice")
sorted_people_tuple = sorted(people_tuple)

print (sorted_people_tuple)






