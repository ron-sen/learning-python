"""
Password Strength Validator
Input password string. Check if it meets rules:length ≥ 8
contains uppercase
contains lowercase
contains digit
contains special char
Print “Strong” / “Weak”. 
"""

password = input("Enter the passsword: ")

#checking lenth of given output

if len(password) < 8:
    print("Weak. Password must be at least 8 characters long,")
else:

    #flag to check rules for password
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    # string of special character storage 
    special_characters = "!@#$%^&*()_+-=[]{}|;:'\",.<>/?`~"

    # loop through each character 
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

# checking if all flags are True

if has_uppercase and has_lowercase and has_digit and has_special:
    print("Strong")
else:
    print("Weak. Password must contain an uppercase letter , a lowecase letter , a digit and a speical character")                     

