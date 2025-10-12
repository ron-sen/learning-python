# chai = "Ginger chai"

# def prepare_chai(order): # passing an arugument 
#     print("Preparing",order)


# prepare_chai(chai)    

chai = [1,2,3]

def edit_chai(cup): # passing a list
    cup[0] = 42

edit_chai(chai)
print(chai) # the list is modified

def make_chai(tea, milk, sugar):
    print(tea,milk,sugar)

make_chai("Darjeeling", "Yes", "Low") #postional arguments
make_chai(tea="Green", sugar="Medium", milk="No") #kwyword arguments

def special_chai(*ingredients, **extras):
    print("Ingrediants", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmom",sweetener = "Honey", foam ="yes")


# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

def chai_order(order = None):
    if order is None:
        order =[]
    print(order)        


chai_order()
chai_order() # this will not modify the default value of order

