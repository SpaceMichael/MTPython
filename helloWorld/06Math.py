import math

print(math.pi)
print(math.e)

radius = float(input('Enter the radius of a circles: '))  # circumference of a circle
circumference = 2 * math.pi * radius
print(circumference)

area = math.pi * pow(radius, 2)  # area of a circle
print(f"The area of the circle is : {round(area, 2)}cm^2")

a = float(input("Enter side A:"))
b = float(input("Enter side B:"))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C ={c}")

friends = 0
friends = friends + 1
friends += 1  # short form
# print(friends)
# friends = 10
# friends = friends - 2
# friends -= 2  # short form
# print(friends)
# friends = 5
# friends **= 2  # short form
# print(friends)
# friends = 9
# remainder = friends % 2  # short form
# print(remainder)
#
# x = 3.14
# y = 4
# z = 5
# result = round(x)
# print(result)
# result = 0
# result = max(x, y, z)
# print(result)
