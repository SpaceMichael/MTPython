# type casting = The process of converting a value of one data type to another
#                          (string, integer, float, boolean)
#                          Explicit vs Implicit / 顯式與隱式
name = "MT"
name2 = ""
age = 19
gpa = 3.4
man = True
print(type(name))
# check name is empty or not
name = bool(name)
print(name)
name2 = bool(name2)
print(name2)
# Explicit vs Implicit / 顯式與隱式

x = 2
y = 2.0

x = x/y
print(x)