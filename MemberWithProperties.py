# MemberWithProperties.py
from dataclasses import dataclass

@dataclass
class Member():
    id:int
    name:str
    email:str
    active:bool
    _age: int

    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError(f"invalid age {value}")
        self._age = value

m = Member(1, "Alice", "alice@gmail.com", True, 21)

print (m)

m.name = "Changed"
# m._age = -99
m.age = -99

print (m.age)

