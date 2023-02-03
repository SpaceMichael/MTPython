#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
# ===list===

# fruits = ["apple", "orange", "banana", "coconut"]
#
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)
# print("cherry" in fruits)
#
# print(fruits)
# print(fruits[0])
# print(fruits[-1])
# print(fruits[::2])
# for fruit in fruits:
#     print(fruit)
#
# fruits[0] = "cherry"
# fruits.append("pineapple")
# fruits.sort()
# for fruit in fruits:
#     print(fruit)

# ====set====
# print("set")
# fruits = {"apple", "orange", "banana", "coconut"}
# print(fruits)
# fruits.add("pineapple")
# print(fruits)
# fruits.pop()
# print(fruits)
# # print(dir(fruits))
# # print(help(fruits))

# ==tuples==
fruits = ("apple", "orange", "banana", "coconut")
print(fruits)
print(fruits.index("apple"))
print(dir(fruits))

