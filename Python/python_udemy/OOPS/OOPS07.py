#compositions
# compositions are for components building use it when a class is built out of other classess ( eg , a car has an engine ) . If u can say A has a B use a composition, its often perferred over inheritance for creating modular and flexible designs.

# compositions : The "has a A" relationship

class Engine:
    def __init__(self , fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        return f"The {self.fuel_type} engine roars to life!"

class Car:
    def __init__(self , color , engine_type):
        self.color = color
        self.engine = Engine(engine_type) # car has an engine object

    def drive(self):
        engine_sound = self.engine.start() #accessing the method of the composed object
        return f"The{self.color} car starts up. {engine_sound}"


# create a Car object with an Engine object inside
my_car = Car("blue", "electric")
print(my_car.drive())
        
                