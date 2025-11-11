# Member.py

# define members using decorators

from dataclasses import dataclass

@dataclass
class Member():
    id:int
    name:str
    email:str
    active:bool

    def __lt__(self, other):
        return self.id < other.id

if __name__ == "__main__":
    m1 = Member(1, "Alice", "alice@gmail.com", True)
    m2 = Member(1, "Alice", "alice@gmail.com", True)

    print (m1)

    members = [m1, m2]

    print (members)

    if m1 == m2:
        print ("same")
    else:
        print ("different")


    if m1 < m2:
        print ("less")



