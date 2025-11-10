# functional_programming_intro.py


# functions are first-class objects in python
# you can treat a function like any other variable


from typing import Callable


def add(a:int, b:int) -> int:
    return a + b

def mul(a:int, b:int) -> int:
    return a * b

def div(a:int, b:int) -> float:
    return a / b

def process(a:int, b:int, func: Callable[[int, int],int]) -> int:
    return func(a, b)

x = 10
y = 20

print (process(x, y, add))
print (process(x, y, mul))
print (process(x, y, div))


sub = lambda x, y : x - y

print (process(x, y, sub))








