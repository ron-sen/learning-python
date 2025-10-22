# comprehensions are stylised version of loop , looks much better for writing beautiful code 

#comprehensions are concise way to crearte lists, sets , dictionaries or generator in python using a single line of code

#where are they  used in real life ?

# well used in production level code 
# filtering item/data 
# transforming data
# create a new collection from an existing one
# flattening nested structure

#if same thing can we do with loop so what's the point of comprehension ?

# cleaner code but not simpler code
# faster execution

# types of comprehensions 
# list ,. set, dictionary, generator

#list comprehension 

menu = [
    "Masala chai ",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea",
]

iced_tea = [tea for tea in menu if "Iced" in tea ]

print(iced_tea)  

actors = [
    "Tom cruise" ,
    "Tom Holland",
    "Tom hank",
    "Daniel day lewis",
    "Daniel radcliff",
    "Chris evans",
    "Chris hemsworth"
]

actor_1 = [actor_1 for actor_1 in actors if "Tom" in actor_1 ]
actor_2 = [actor_2 for actor_2 in actors if "Daniel" in actor_2 ]
actor_3 = [actor_3 for actor_3 in actors if "Chris" in actor_3 ]


print(actor_1)
print(actor_2)
print(actor_3 )
