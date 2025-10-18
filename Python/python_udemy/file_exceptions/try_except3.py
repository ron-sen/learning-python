def process_order(item , qunatity):
    try:
        price = {"masala": 20}[item]
        cost = price * qunatity 
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger", 2)
process_order("masala","two")                