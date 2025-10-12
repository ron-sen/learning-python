#namespace

class Chai :
    origin = "India" #properties 

print(Chai.origin)

Chai.is_hot = True #adding properties outside class
print(Chai.is_hot)

# creating object from class chai

masala = Chai() #object creation
print(masala.origin)
print(masala.is_hot)

# now chaging the object proprerty does not affect class and other objects 

masala.is_hot = False

print("Class: ", Chai.is_hot)
print(f"Masala {masala.is_hot}")

masala.flavour = "Masala"
print(masala.flavour)