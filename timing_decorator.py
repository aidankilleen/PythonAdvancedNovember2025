# timing_decorator.py
import time

def timing(func):

    def wrapper(*args, **kwargs):
        print ("wrapper started")

        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print (f"function took: {end_time - start_time:.5f}s")

        print ("wrapper finished")
    return wrapper

@timing
def do_something():
    print ("starting...")
    time.sleep(5)
    print ("finished")

do_something()



