Small = 10
Medium = 15
Large  = 20

Cup_size = str(input("Enter the cup size : ")).lower()

if Cup_size == "small":
    print(f"Your cup size is {Cup_size} and the price is {Small}")

elif Cup_size == "medium":
    print(f"Your cup size is {Cup_size} and the price is {Medium}")

elif Cup_size == "large" :
    print(f"Your cup size is {Cup_size} and the price is {Large}")

else:
    print("Invalid cup size entered , please try again !")        