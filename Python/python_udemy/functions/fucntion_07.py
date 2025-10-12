# non local scope means that inside a nested function, you can modify a variable from the enclosing scope

def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print(f"After kitchen update", chai_type)    

update_order()
    


