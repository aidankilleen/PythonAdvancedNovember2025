# generator_investigation.py

# this function returns a generator
def count_up_to(n):
    print("count_up_to called")
    count = 1

    while count <= n:
        yield count
        print (f"looped {count}")
        count += 1

g = count_up_to(10)

#print (next(g))
#print (next(g))
#print (next(g))

for n in g:
    print (n)













