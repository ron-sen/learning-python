#Dictionary
# Create a dictionary with some initial key-value pairs
chai_order = dict(type = "Masala chai",size = "Large",  price = "50")
print(chai_order)

chai_recipe = {}  #another  way to create an empty dictionary

chai_recipe["base"] = "balck tea" #adding a key-value pair #in brackets we define the key and after equal sign we define the value
chai_recipe["liquid"] = "milk"

print(chai_recipe['base'])#accessing a value using its key
print(chai_recipe["liquid"])


#Memmber sip test

print(f"Is sugar in the order? {'sugar' in chai_order}") # checking if a key exists in the dictionary 

chai_order = {"type": "Ginger Chai", "size": "Medium", "price":40}

print(f"Order details: (keys): {chai_order.keys()}")# getting all the key names in the dictionary # keys() -- is that how we call a function
print(f"Order details: (values): {chai_order.values()}") #getting all the values in the dictionary 
print(f"Order details: (items): {chai_order.items()}")#getting all the key value pairs in the dictionary # this returns a list of tuples.

last_item = chai_order.popitem()
print(f"Removed last item :{last_item}") 

extra_spices = {"cardamom": "crushed", "ginger": "fresh"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

chai_size = chai_order["size"]
print(f"Chai size: {chai_size}") #output  is "Medium"

customer_note = chai_order.get("note", "No note provided") 
print(f"Customer note is : {customer_note}") 