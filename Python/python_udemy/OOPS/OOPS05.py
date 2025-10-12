#init function -- inititalization
# __init__ initiate an object for me , init is a resevered keywords
# and they way u define it is by a constructor 

class Artwroks :
    def __init__(self , type_ ,charges ): #self is used of course
        self.type = type_
        self.charges = charges
    

    def summary(self):
        return f"{self.charges} for {self.type} art"
    

order = Artwroks("Digital", 5000)
print(order.summary())

order_sec = Artwroks("Traditional", 2000)
print(order_sec.summary())