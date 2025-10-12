#set compresshenions

favourite_chai = [
    "Masala chai" , "Green tea", "Ginger tea", 
    "Lemon tea", "Elaichi chai",

]

unique_chai = { chai for chai in favourite_chai }
print(unique_chai)

# complex example

recipes = {
    "Masala chai": ["ginger", "cardmom", "clove"],
    "Elaichi chai": ["cardmom", "milk"],
    "Spicy chai": ["ginger","black pepper", "clove"],

}

unique_spices = { spice for ingredients in recipes.values() for spice in ingredients }

print(unique_spices)
