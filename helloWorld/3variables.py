# variable = reusable for storing a value
# INTEGER FLOAT STRING BOOLEAN NONE

first_name = "Bro"
last_name = "Code"
full_name = first_name + " " + last_name
# print(type(name))
print("Hello !!!" + full_name)
# print int
age = 21
print("Hello Int :D")
print(age)
print("Hello Int " + str(age) + ' ^_^')
# separate arguments
print("Hello Int", age, '^_^')
# f -string
print(f"Hello Int {age} ^_^")
# 4 basic data types  integers, floats, strings , booleans
players = 2
quantity = 5
print(f"You are {age} years old")
print(f"There are {players} online")
print(f"You will buy {quantity} items")
gpa = 3.9
print(f"Your GPA is {gpa}")
print(f"Hello {full_name} -.-")
online = True
offline = False
print(f"Are you online : {online}")
print(f"Are you online : {offline}")

# if statement if elif else
if online:
    print("you are online")
else:
    print("u are offline")

# tips & tricks
x, y, z = 1, 2, 3
a = b = c = 0
print(f"{x},{y},{z}")
print(f"{a},{b},{c}")
# None
e = None
print(e is True)
print(e is False)
