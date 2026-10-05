
import random

def roll_dice():
    return random.randint(1,6)
roll = 0 
while roll != 6:
    roll = roll_dice()
    print(f"rolled: {roll}")


import random

def roll_dice(sides):
    return random.randint(1,sides)

sides = int(input("how many sides are there"))
roll = 0 
while roll != sides:
    roll = roll_dice(sides)
    print(f"Rolled: {roll}")

def gall_leters(gallons):
    return gallons*3.785
gallons = float(input("enter how much "))

while gallons >= 0:
    leters = gall_leters(gallons)
    print(f"{gallons} gallons is {leters:.2f} leters")
    gallons = float(input("enter how much "))


def sum_list(numbers):
    total = 0 
    for number in numbers:
        total = total + number
    return total 
numbers = [4,8,12,16,32,64]
result = sum_list(numbers)
print(f"The sum of the list is {result}")

def remove_odd(numbers):
    even=[]
    for number in numbers:
        if number% 2 == 0:
            even.append(number)
    return even
first = [1,2,3,4,5,6,7,8,9,10]
final = remove_odd(first)
print(f"the original list was {first} now the list without the odd numbers is {final}")

import math


def unit_price(diameter_cm, price):
    radius_m = (diameter_cm / 100) / 2
    area = math.pi * radius_m ** 2
    return price / area


diameter1 = float(input("Enter the diameter of pizza 1 (cm): "))
price1 = float(input("Enter the price of pizza 1 (eur): "))
diameter2 = float(input("Enter the diameter of pizza 2 (cm): "))
price2 = float(input("Enter the price of pizza 2 (eur): "))

unit1 = unit_price(diameter1, price1)
unit2 = unit_price(diameter2, price2)

print(f"Pizza 1 costs {unit1:.2f} eur per square meter")
print(f"Pizza 2 costs {unit2:.2f} eur per square meter")

if unit1 < unit2:
    print("Pizza 1 provides better value for money.")
elif unit2 < unit1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")
