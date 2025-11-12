# strategy_investigation.py

# python natively supports the strategy pattern
# because functions are first class objects
# and can be passed to functions

def add(a, b):
    return a+b

def mul(a, b):
    return a*b

def process(a, b, func):
    return func(a, b)

print (process(10, 20, add))
print (process(10, 20, mul))


# design patterns

# decorator - native feature in python
# builder - see builder_investigation.py
# strategy - supply a function to be run on some operands
# facade - Provides a simplified interface to a library - MemberDao - provides a simple
# interface to the database (users don't need to know sql to be able to use it)



    
