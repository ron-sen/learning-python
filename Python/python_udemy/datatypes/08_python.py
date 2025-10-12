# List , mutable datatype
# Lists are mutable, meaning they can be changed after creation.
# There are so many methods available for lists.


ingredients = ["Water", "Milk" , "black tea"]
ingredients.append("Sugar")    #always adds to the end of the list 
print(f"Ingredients: {ingredients}")
ingredients.remove("Water")
print(f"Ingredients: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingrediants = ["Water", "Milk"]

chai_ingrediants.extend(spice_options)  #combining lists 
print(f"chai : {chai_ingrediants}")

#indexing in list is the individual elements of the list

chai_ingrediants.insert(2, "black tea")
print(f"chai :{chai_ingrediants}")

last_added = chai_ingrediants.pop()  #removes the last element and returns it
print(f"{last_added}" )
print(f"chai :{chai_ingrediants}")
chai_ingrediants.reverse()
print(f"chai: {chai_ingrediants.reverse()}")

chai_ingrediants.sort() #sorts the list in ascending order
print(f"Chai: {chai_ingrediants}")

sugar_levels = [1,2,3,4,5]
print(f"Maximum suagarlevel: {max(sugar_levels)}")
print(f"Minimum sigar level: {min(sugar_levels)}")

# operator overloading

base_liquid = ["water", "milj"]
extra_flavours = ["ginger", "cardamom"]

full_liquid_mix  = base_liquid + extra_flavours # This combines the two lists into one
print(f"Full liquid mix: {full_liquid_mix}")

strong_brew = ["brew tea", "Water"] * 3 
print(f"string brew: {strong_brew}")

#from operator import itemgetter 

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Raw spice data: {raw_spice_data}")  