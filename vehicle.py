# assign  2: Polymorphism with Vehicles
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self): 
        print(f"{self.brand} {self.model} is moving generically.")

# Subclass: Car
class Car(Vehicle):
    def move(self): 
        print(f"{self.brand} {self.model} is driving on the road!")

# Subclass: Plane
class Plane(Vehicle):
    def move(self): 
        print(f"{self.brand} {self.model} is flying through the skies!")

# Subclass: Boat 
class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is sailing on the water!")

# Demo: List of vehicles,
if __name__ == "__main__":
    vehicles = [
        Car("Toyota", "Camry"),
        Plane("Boeing", "747"),
        Boat("Yamaha", "WaveRunner"),
        Vehicle("Generic", "Wagon")  
    ]
    
    print("Polymorphism in Action: Calling move() on each vehicle...")
    for vehicle in vehicles:
        vehicle.move() 