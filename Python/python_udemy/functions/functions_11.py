# types of functions
# pure vs impure functions
# recursive functions
# lambda functions (anonymous functions)    

# pure vs impure functions

def pure_chai(cups):
    return cups * 10

total_chai = 0

#not recommended

def impure_chai(cups):
    global total_chai
    total_chai += cups  


# recursive functions - a function that calls iteself    

def pour_chai(n):
    print(n)
    if n == 0:
        return "All chai is poured"
    return pour_chai(n -1)

print(pour_chai(5))

# lamda functions (anonomus functions)

chai_type = ["light", "Kadak", "ginger", "Kadak"]

strong_chai = list(filter(lambda chai: chai =="Kadak", chai_type))

print(strong_chai) 