import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0 
        self.travel_distance = 0 
car = Car ("ABC-123", 142)
print(f"Registrarion number = {car.registration_number}")
print(f"Max speed : {car.maximum_speed}km/h)")
print(f"Current speed: {car.current_speed} km/h")
print(f"Travelled distance: {car.travelled_distance} km")




class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0 
        self.travel_distance = 0 
        
    def accelrate(self,change):
        new_speed = self.current_speed + change
        if new_speed > self.maximum_speed:
            new_speed = self.maximum_speed
        elif new_speed < 0:
            new_speed = 0 
        self.current_speed = new_speed
car = Car ("ABC-123", 142)
car.accelrate(70)
car.accelrate(50)
car.accelrate(30)
print("the current speed is", car.current_speed,"km/h")
car.accelerate(-200)
print("the final speed is", car.current_speed,"km/h")



class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0 
        self.travel_distance = 0 
        
    def accelrate(self,change):
        new_speed = self.current_speed + change
        if new_speed > self.maximum_speed:
            new_speed = self.maximum_speed
        elif new_speed < 0:
            new_speed = 0 
        self.current_speed = new_speed
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
car = Car("ABC-123", 142)

car.accelerate(60)
car.drive(1.5)
print("the travel distance is", car.travelled_distance, "km/h")

import random

cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

while max(car.travelled_distance for car in cars) < 10000:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

print("Registration  Max speed  Speed  Distance")
for car in cars:
    print(f"{car.registration_number:<14}{car.maximum_speed:<11}{car.current_speed:<7}{car.travelled_distance}")

