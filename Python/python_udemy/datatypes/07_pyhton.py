#Tuples
masala_spices = ("cardamom", "cinnamon", "cloves")

(spice1, spice2 , spice3)= masala_spices 

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio , cardamom_ratio = 2 , 1 
print(f"Ratio is G :{ginger_ratio} C : {cardamom_ratio}")
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio  # Swapping values
print(f"Ratio is G :{ginger_ratio} C : {cardamom_ratio}")

# Tuples are immutable, so we cannot change them
#Memmber ship testing

print(f"Is cinnamon in masala spices? {'cinnamon' in masala_spices}")
