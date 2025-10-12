#scopes  - global and local

def serve_chai():
    chai_type = "Masala" #local scope
    print(f"Inside function {chai_type}")


chai_type = "Lemon" #global scope , that is outside the function
serve_chai()
print(f"Outside function {chai_type}") 
# The local variable chai_type inside serve_chai() does not affect the global variable chai_type

#nested fucntions

def chai_counter():
    chai_order = "lemon" #enclosing scope
    def print_Order():
        chai_order = "Ginger"
        print("Inner:", chai_order)
    print_Order()
    print("Outer:", chai_order)


chai_order = "Tulsi" #global scope
chai_counter()
print("Global:", chai_order)    