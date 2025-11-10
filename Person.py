
class Person():

    def __init__(self, id=0, name="", email="", active=False):
        self.id = id
        self.name = name
        self.email = email
        self.active = active
        pass

    def __str__(self):
        return f"{self.id} - {self.name} - {self.email} {"Active" if self.active else "Inactive"}"

    def __repr__(self):
        #return f"[{self.id}, {self.name}, {self.email}, {self.active}]"
        return self.__str__()

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.email == other.email and self.active == other.active

    def __lt__(self, other):
        # print (f"comparing {self.id} with {other.id}")
        return self.id < other.id


if __name__ == "__main__":
    print (__name__)
    # new person object p
    p1 = Person(1, "Alice", "alice@gmail.com", True)
    p2 = Person(1, "Alice", "alice@gmail.com", True)
    #p2 = p1

    print (p1)

    print(id(p1))
    print(id(p2))

    if p1 == p2:
        print ("same")
    else:
        print ("different")
