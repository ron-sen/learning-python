# infinite generators

def chai_coustomer():
    print("Welcome ! what chai would you like ?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield 


stall = chai_coustomer()
next(stall) # start the generator

stall.send("Masala chai")
all.send("Ginger chai")