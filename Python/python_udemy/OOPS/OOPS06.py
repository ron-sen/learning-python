# inheritance
# inheritance is for specialization , use it when a new class is a specific kind of an exisiting class , if we are saying A is a B , we use inheritance.
# iheritance : the "Is A" relationship

#parent class
class Vehicles:
    def __init__(self, color , wheels):
        self.color = color
        self.wheels = wheels

    def honk(self):
        return "Beep beep !"
    
# child class inheriting from vehicle

class Car(Vehicles):
    def __init__(self, color , wheels , model):
        super().__init__(color, wheels) # this  call the parents constructor
        self.model = model

    def drive(self):
        return f"The {self.color} {self.model} is driving on its {self.wheels} wheels."


# create a car object
my_car = Car("red", 4 , "Tesla")
print(my_car.drive())
print(my_car.honk())        




