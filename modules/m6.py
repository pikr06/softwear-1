import random

count = int(input("How many dice to roll? "))

total = 0
for i in range(count):
    total += random.randint(1, 6)

print("The sum of the dice is", total)



numbers = []

while True:
    text = input("Enter a number  ")
    if text == "":
        break
    numbers.append(float(text))

numbers.sort(reverse=True)
print("The five greatest numbers:")
for n in numbers[:5]:
    print(n)



n = int(input("Enter an integer: "))

prime = n > 1

for i in range(2, n):
    if n % i == 0:
        prime = False
        break

if prime:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")


    cities = []

for i in range(5):
    name = input("Enter the name of a city: ")
    cities.append(name)

print("You entered these cities:")
for city in cities:
    print(city)