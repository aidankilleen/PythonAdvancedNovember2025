# Team.py

from Person import Person


class Team():

    def __init__(self, name):
        self.name = name
        self.members = []
    
    def add(self, person):
        self.members.append(person)

    def __str__(self):
        
        return " ".join(member.name for member in self)
        
        #names = ""
        #for member in self.members:
        #    names += f" {member.name} "
        #return names
    
    def __len__(self):
        return len(self.members)

    def __iter__(self):
        return iter(self.members)
    
    def __getitem__(self, i):
        return self.members[i]
    
if __name__ == "__main__":

    t = Team("Corporate Sales")
    t.add(Person(9, "Dan", "dan@gmail.com", False))
    t.add(Person(15, "Alice", "alice@gmail.com", True))
    t.add(Person(2, "Carol", "carol@gmail.com", True))
    t.add(Person(12, "Bob", "bob@gmail.com", False))
    t.add(Person(18, "eve", "eve@gmail.com", True))
    print (t)

    print (len(t))

    for member in t:
        print (member)

    print ("*" * 30)
    print (t[0])
    print (t[-1])

    print (t[1:3])

    print (t[::-1])















    

    