
class Publication:
    def __init__(self, name):
        self.name = name
 
 
class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages
 
    def print_information(self):
        print("Book")
        print("Name:", self.name)
        print("Author:", self.author)
        print("Pages:", self.pages)
        print()
 
 
class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
 
    def print_information(self):
        print("Magazine")
        print("Name:", self.name)
        print("Chief editor:", self.chief_editor)
        print()
 
 
magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No. 6", "Rosa Liksom", 192)
 
magazine.print_information()
book.print_information()


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
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
 
 
class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity
 
 
class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume
 
 
electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)
 
electric_car.accelerate(100)
gasoline_car.accelerate(120)
 
electric_car.drive(3)
gasoline_car.drive(3)
 
print("Electric car", electric_car.registration_number, ":", electric_car.distance, "km")
print("Gasoline car", gasoline_car.registration_number, ":", gasoline_car.distance, "km")