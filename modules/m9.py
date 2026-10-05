class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0 
        self.travel_distance = 0 
    car = Car("ABC-123", 142)
    print(f"Registrarion number = {car.registration_number}")
    print(f"Max speed : {car.maimum_speed}km/h)")
    print(f"Current speed: {car.current_speed} km/h")
    print(f"Travelled distance: {car.travelled_distance} km")
