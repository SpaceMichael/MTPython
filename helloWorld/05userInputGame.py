# user input
name = input("Enter your name:")
age = int(input("Enter your age:"))
age = age + 1
print(f"your name is {name}")
print(f"your age is {age}")

# mal libs game

adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective of mine: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}.")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}!")

#  Volume / AREA CALC
length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))
height = float(input("Enter the height of a rectangle: "))

volume = length * width * height

print(f"The volume is : {volume}cm^3")

# EXERCISE 3 SHOPPING CART
item = input("what item would u like to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("How many/much would you like?:"))

total = price * quantity
print(f" You have bought {quantity} X {item}/s")
print(f"Your total price is : $ {round(total)}")
