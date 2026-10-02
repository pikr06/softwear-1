#def greet(greeting, times=1):
#    for i in range(times):
#        print(greeting + " " + str(i+1) + ". time")
#    return

#greet(hello,5)
#greet(greeting, times=3)


#def greeting ():
#    print("my name is pikr")
#greeting()


#def addition (num1,num2):
#    addition = int((num1 + num2))
#    print(addition)
#addition(1003,3943)

#def greetings (name):
#  print("hello",name)

#name = input("hallo")
#greetings(name)


#def greet (greeting,times):
   
#   for number in range(times):
#      print(greeting,times)
#greet("piyush",4)


#Create a new class Field, with an initializer for it. T
# he initializer defines he properties
# 
#  field_id, name, and description for Field objects. All three are given as parameters.

class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.sound)
        return


dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")

dog1.bark(2)
dog2.bark(5)