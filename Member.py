# Member.py

# define members using decorators

from dataclasses import dataclass

@dataclass
class Member():
    id:int
    name:str
    email:str
    active:bool

m1 = Member(1, "Alice", "alice@gmail.com", True)
m2 = Member(1, "Alice", "alice@gmail.com", True)

print (m1)

members = [m1, m2]

print (members)

if m1 == m2:
    print ("same")
else:
    print ("different")




