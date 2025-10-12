#infinte generators

def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1


refill = infinite_chai() 
user2 = infinite_chai()

for _ in range(10): # the underscore is used when we don't care about the variable
    print(next(refill))


for _ in range(6):
    print(next(user2))