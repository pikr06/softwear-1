#class dog:
#    def __init__(self, name, breed):
#        self.name = name
#        self.breed = breed
#dog1 = dog("buddy", "husky")
#print(f"dog's name:{dog1.name}, breed: {dog1.breed}")



#class Dog:
#    def __init__(self, name, birth_year, sound="Woof woof"):
#        self.name = name
#        self.birth_year = birth_year
#        self.sound = sound

#    def bark(self, times):
#        for i in range(times):
#            print(self.sound)
#        return


#dog1 = Dog("Rascal", 2018)
#dog2 = Dog("Boi", 2022, "Yip yip yip")

#dog1.bark(2)
#dog2.bark(5)



class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0


def main():
    car = Car("ABC-123", 142)

    print("Registration number:", car.registration_number)
    print("Maximum speed:", car.max_speed)
    print("Current speed:", car.current_speed)
    print("Travelled distance:", car.travelled_distance)

    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print("Current speed:", car.current_speed)

    car.accelerate(-200)
    print("Final speed:", car.current_speed)


if __name__ == "__main__":
    main()
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0


def main():
    car = Car("ABC-123", 142)

    print("Registration number:", car.registration_number)
    print("Maximum speed:", car.max_speed)
    print("Current speed:", car.current_speed)
    print("Travelled distance:", car.travelled_distance)

    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print("Current speed:", car.current_speed)

    car.accelerate(-200)
    print("Final speed:", car.current_speed)


if __name__ == "__main__":
    main()   