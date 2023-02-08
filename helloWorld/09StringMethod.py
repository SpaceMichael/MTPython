# -------------------------------
# STRING METHODS
# -------------------------------
name = input("Enter your name: ")
# phone_number = input("Enter your phone #: ")

# length = len(name)
result = len(name)
print(result)
# print(help(str))
# index = name.find(" ")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count(" ")
# phone_number = phone_number.replace("-", "")

# -------------------------------
#        EXERCISE
# -------------------------------
username = input("Enter a username: ")

if len(username) > 12:
    print("Your name can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain digits")
else:
    print(f"Welcome {username}!")

# indexing = accessing elements of a sequence using [] (indexing operator)
#                     [start : end : step]
credit_number = "1234-5678-9012-3456"
print(f"full credit_numer {credit_number}")
print(f"credit_number[0] {credit_number[0]}")  # [start : end : step]
print(f"credit_number[0:4] {credit_number[0:4]}")
print(f"credit_number[:4] {credit_number[:4]}")
print(f"credit_number[4:8] {credit_number[4:8]}")
print(f"credit_number[4:] {credit_number[4:]}")
print(f"credit_number[-1] {credit_number[-1]}")
print(f"credit_number[-4:] {credit_number[-4:]}")
print(f"XXXX-XXXX-XXXX-{credit_number[-4:]}")
print(f"credit_number[::2] {credit_number[::2]}")
print(f"credit_number[::3] {credit_number[::3]}")
# email slicer exercise index usage

email = input("Enter your email: ")
username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username} and domain is {domain}")

# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format

price1 = 3.14159
price2 = -987000.65
price3 = 12.34
print(f"price1 is: ${price1:}")
print(f"price1 is: ${price1:+}")
print(f"price1 is: ${price1:.3f}")
print(f"price1 is: ${price1:10}")
print(f"price2 is: ${price2:+,.2f}")
print(f"price2 is: ${price2:010}")
print(f"price2 is: ${price2:,}")
print(f"price2 is: ${price2:>10}")
print(f"price2 is: ${price2:.1f}")
print(f"price3 is: ${price3:}")

# while loop = perform some code WHILE some condition remains true

# ---------------- EXAMPLE 1 ----------------

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name!")
    name = input("Enter your name: ")

print(f"Hello {name}")

# ---------------- EXAMPLE 2 ----------------

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

# ---------------- EXAMPLE 3 ----------------

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")

# ---------------- EXAMPLE 4 ----------------

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"You picked the number {num}")

# Python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")

# For loops in Python are easy
# for loops = execute a block of code a fixed number of times.
#                     You can iterate over a range, string, sequence, etc.

# ---------------- EXAMPLE 1 ----------------
print(f"For loops in Python")

for x in range(1, 11):
    print(x)

# ---------------- EXAMPLE 2 ----------------

for x in reversed(range(1, 11)):
    print(x)

print("Happy New Year!")

# ---------------- EXAMPLE 3 ----------------

for x in range(1, 11, 2):
    print(x)

# ---------------- EXAMPLE 4 ----------------

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

# ---------------- CONTINUE ----------------

for x in range(1, 21):
    if x == 13:  # skip unlucky 13
        continue
    else:
        print(x)

# ---------------- BREAK ----------------

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)
# nested loop = A loop within another loop (outer, inner)
#                          outer loop:
#                              inner loop:

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
#
