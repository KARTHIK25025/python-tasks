class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
class Car(Vehicle):
    def display(self):
        print(f"Car Brand: {self.brand} | Max Speed: {self.speed} km/h")
class Bike(Vehicle):
    def display(self):
        print(f"Bike Brand: {self.brand} | Max Speed: {self.speed} km/h")
car = Car("Toyota", 180)
bike = Bike("Yamaha", 80)
car.display()
bike.display()
