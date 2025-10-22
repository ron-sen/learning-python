file = open("order.txt","w") # loaded the file in memory
#file.write("good morning") # writing in memory 
 # some problems could occur 

 #better is 

try :
    file.write("Good morning")
finally:
    file.close()


#new way in python wihtout using try and except

with open("order.txt", "w") as file:
    file.write("Good after noon")

#what actullay happens 

'''
file 

file.__enter__()

file.__exit__()

'''