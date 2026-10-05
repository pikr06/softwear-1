class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor
 
    def floor_up(self):
        self.floor = self.floor + 1
        print("Floor", self.floor)
 
    def floor_down(self):
        self.floor = self.floor - 1
        print("Floor", self.floor)
 
    def go_to_floor(self, target_floor):
        while self.floor < target_floor:
            self.floor_up()
        while self.floor > target_floor:
            self.floor_down()
 
 
elevator = Elevator(1, 10)
elevator.go_to_floor(5)
elevator.go_to_floor(1)
 
 
 class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor
 
    def floor_up(self):
        self.floor = self.floor + 1
        print("Floor", self.floor)
 
    def floor_down(self):
        self.floor = self.floor - 1
        print("Floor", self.floor)
 
    def go_to_floor(self, target_floor):
        while self.floor < target_floor:
            self.floor_up()
        while self.floor > target_floor:
            self.floor_down()
 
 
class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for number in range(elevator_count):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)
 
    def run_elevator(self, elevator_number, target_floor):
        print("Elevator", elevator_number)
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(target_floor)
 
 
building = Building(1, 10, 3)
building.run_elevator(1, 5)
building.run_elevator(2, 8)


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor
 
    def floor_up(self):
        self.floor = self.floor + 1
        print("Floor", self.floor)
 
    def floor_down(self):
        self.floor = self.floor - 1
        print("Floor", self.floor)
 
    def go_to_floor(self, target_floor):
        while self.floor < target_floor:
            self.floor_up()
        while self.floor > target_floor:
            self.floor_down()
 
 
class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for number in range(elevator_count):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)
 
    def run_elevator(self, elevator_number, target_floor):
        print("Elevator", elevator_number)
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(target_floor)
 
    def fire_alarm(self):
        print("FIRE ALARM!")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)
 
 
building = Building(1, 10, 3)
building.run_elevator(1, 5)
building.run_elevator(2, 8)
building.fire_alarm()


import random
 
 
class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0
 
    def accelerate(self, change):
        self.speed = self.speed + change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0
 
    def drive(self, hours):
        self.distance = self.distance + self.speed * hours
 
 
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
 
    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)
 
    def print_status(self):
        print(self.name)
        print("Car       Max speed   Speed   Distance")
        for car in self.cars:
            print(f"{car.name:<10}{car.max_speed:<12}{car.speed:<8}{car.distance}")
        print()
 
    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False
 
 
cars = []
for number in range(1, 11):
    max_speed = random.randint(100, 200)
    car = Car("ABC-" + str(number), max_speed)
    cars.append(car)
 
race = Race("Grand Demolition Derby", 8000, cars)
 
hours = 0
while not race.race_finished():
    race.hour_passes()
    hours = hours + 1
    if hours % 10 == 0:
        race.print_status()
 
race.print_status()