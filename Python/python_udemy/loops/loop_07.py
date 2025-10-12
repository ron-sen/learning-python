# out of order

flavours = ["Ginger", "Out of stock","Lemon","Discountinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")

print(f"Out side of loop")    