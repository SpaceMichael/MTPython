# if = Do some code IF condition is True
# else = Do something else if above condition/s are False

age = int(input("Enter your age: "))

if age >= 100:
    print("you are too old to sign up!")
elif age < 0:
    print("you haven't been born yet!")
elif age >= 18:
    print("You are now sign up!")
else:
    print("You must be 18+ to sign up!")

# example

name = input("Enter your name: ")

if name == "":
    print("You did not enter your name!")
else:
    print(f"Hello {name}")
# example

online = False
if online:
    print("You are online")
else:
    print("You are offline")
