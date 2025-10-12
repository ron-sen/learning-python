#attribut shadowing

#objects from classess are varibles/attributes  both are exchangable

#when it goes in object or class its called  attribute

class School:
    icse = "elite"
    cbse = "very good"
    state_board = "good"


boards = School() #creating object
print(boards.icse)

boards.state_board = "not too good"
boards.ivy_schools = "US schools"
print("After changing state board ", boards.state_board)
print("Direct look into the class", School.state_board)

del boards.state_board #deletion 
del boards.ivy_schools
print(boards.ivy_schools)  # u recieve an attribute error because the ivy_schools are not in class
print(boards.state_board)
# so in deletion the value of statebaord is no longer in object board but still in the classess , and that's what it prints
