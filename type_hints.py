# type_hints.py
name:str = "Aidan"
name = 99

i = 10
print (i)

# python traditionally isn't strongly typed
i = "ten"
print (i)

def generate_greeting(name:str) -> str:
    return f"Welcome {name}"

i:int
i = generate_greeting(27)


people: list[str] = []

#people = [1, 2, 3]

people.append("Alice")
people.append(1)


print (people)





