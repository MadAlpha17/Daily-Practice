class Vehicle:
    def __init__(self,name,max_speed , mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
class Truck(Vehicle):
    pass
class Bus(Vehicle):
    def seating_capacity(self, capacity):
        self.capacity = capacity
        return super().seating_capacity(capacity)

truck1=Truck("TATA",150,10)
bus1=Bus("Volvo", 180, 12)
print("Vehicle Name:", truck1.name, "|| MaxSpeed:", truck1.max_speed, "|| Mileage:", truck1.mileage)
print("Vehicle Name:", bus1.name, "|| MaxSpeed:", bus1.max_speed, "|| Mileage:", bus1.mileage)
print(bus1.seating_capacity(20))