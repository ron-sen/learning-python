
#Sets

essential_spice = {"cardamom", "ginger","cinnamon"}
optional_spice = {"cinnamon", "ginger", "pepper"}

all_spices = essential_spice | optional_spice # Union of sets
print(all_spices)

common_spices = essential_spice & optional_spice # Intersection of sets
print(common_spices)

common_spices = essential_spice - optional_spice # Difference of sets
print(common_spices)