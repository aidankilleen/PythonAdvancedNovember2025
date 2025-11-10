# decorator_investigation.py

# loud is a decorator (function that takes in a function and returns a different function)
# modifies the operation of the original function 
# without modifying the original function in any way
def loud(func):
    def wrapper():
        message = func()
        return message.upper()
    return wrapper

@loud
def greet():
    return "hello"

print (greet())


# decorator that takes parameters
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(5)
def hello(name):
    print(f"Hello {name}")

hello("Alice")



