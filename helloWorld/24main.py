# coding =utf-8
# module = a file containing code u want to include in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files

# ---------- main.py ----------
import example
# import math
# print(math.pi)

# import math as m
# print(m.pi)

# from math import pi
# print(pi)

result = example.pi
result = example.square(3)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)

# print(help("modules"))
# print(help("math"))
print(result)
