#improving  readability

def calculate_bill(cups , price_per_cup):
    return cups*price_per_cup



my_bill = calculate_bill(3,15) # here the function is returning a value that we save in a variable
print(my_bill)

#another way to do this is to print the value directly

print("Order for table 2 :", calculate_bill(2,50))  