#boolean

is_boiling = True
stir_count = 5 
total_actions = stir_count + is_boiling #uppercasting
print(f"Total actions: {total_actions}")  

milk_present = None # None or 0 = false
print(f"Milk present: {bool(milk_present)}")  

#Logical operations
    #and or not 

water_hot = True
tea_added = True

can_serve = water_hot and tea_added
print(f"Can serve chai : {can_serve}")


 