#string immutable ( cant be changed)
# core , indexing, slicing 

chai_type = "Ginger chai"
customer_name = "John Doe"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description  = "Doctor and engineer"

print(f"First word: {chai_description[0:19:2]}")  # Slicing 0 is beginning, 8 is end, 2 is means it keeps A skips r then have o and skips m and so on 

#pythonic way of  doing it  [:8]  output Aromatic

print(f"Last word: {chai_description[12:]}")  # Slicing from 12 to end

print(f"Last word: {chai_description[::-1]}")  # Slicing from end to start, reverse the string output is dloB dna citamorA  string reversing 

label_text = "chai S̤pecial"
encode_label = label_text.encode('utf-8')  # Encoding the string to bytes
print(f"Non Encoded label: {label_text}") 
print(f"Encoded label: {encode_label}") 

decoded_label = encode_label.decode('utf-8')  # Decoding the bytes back to string
print(f"Decoded label: {decoded_label}") 