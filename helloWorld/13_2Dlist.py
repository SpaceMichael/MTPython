# Here are a few different 2d collection combinations:

fruits = ["apple", "orange", "banana"]
vegetables = ["celery", "carrot"]
meat = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meat]
print(groceries)
print(groceries[1][1])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# 2D list of lists
num_pad = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"]]
print('List case')
for row in num_pad:
    print(row, end=" ")
    print()


# 2D list of tuples
num_pad = [(1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")]
print('tuples case')
for row in num_pad:
    print(row, end=" ")
    print()


# 2D list of sets
num_pad = [{1, 2, 3},
           {4, 5, 6},
           {7, 8, 9},
           {"*", 0, "#"}]
print('set case')
for row in num_pad:
    print(row, end=" ")
    print()

# 2D tuple of lists
num_pad = ([1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"])
print('tuple of list case')
for row in num_pad:
    print(row, end=" ")
    print()

# 2D tuple of tuples
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

print('tuple of tuple case')
for row in num_pad:
    print(row, end=" ")
    print()

# 2D tuple of sets
num_pad = ({1, 2, 3},
           {4, 5, 6},
           {7, 8, 9},
           {"*", 0, "#"})

print('tuple of set case')
for row in num_pad:
    print(row, end=" ")
    print()

# # 2D set of lists (NOT VALID)
# num_pad = {[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9],
#            ["*", 0, "#"]}

# 2D set of tuples
num_pad = {(1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")}


print('set of tuple case')
for row in num_pad:
    print(row, end=" ")
    print()

# # 2D set of sets (NOT VALID)
# num_pad = {{1, 2, 3},
#            {4, 5, 6},
#            {7, 8, 9},
#            {"*", 0, "#"}}
print("final")
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

