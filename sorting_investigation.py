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
    Person(11, "Alice", "alice@gmail.com", True), 
    Person(9, "Dan", "dan@gmail.com", False),
    Person(15, "Alice", "alice@gmail.com", True),
    Person(2, "Carol", "carol@gmail.com", True),
    Person(12, "Bob", "bob@gmail.com", False)    
]

def get_sort_key(person):
    return person.id

people.sort(key=get_sort_key)

print (people)











