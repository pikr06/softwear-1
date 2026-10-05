n = 1 
while n <= 1000:
    if n % 3 == 0:
        print(n)
    n += 1

while True:
    inch = float(input("Enter inches"))
    if inch < 0:
        break
    print(f"{inch} = {inch*2.54}cm")

numbers = []

while True:
    number = input("enter a num")
    if number == "":
        break
    numbers.append(float(number))

if numbers:
    print(f"smallest = {min(numbers)}")
    print(f"largest = {max(numbers)}")
else:
    print("No numbers entered.")

import random

number = random.randint(1,10)
while True:
    guess = int(input("guess a number between 1 and 10 "))
    if number > guess:
        print("nope too high")
    elif number < guess:
        print("nope too low")
    else:
        print("corret")

attempts = 0

while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")
    if username == "python" and password == "rules":
        print("Welcome")
        break
    attempts += 1

if attempts == 5:
    print("Access denied")