# coding =utf-8
# exception =   events detected during execution that interrupt the flow of a program
import time
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:  # 0
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:  # char
    print(e)
    print("Enter only numbers plz")
except Exception as e:  # as e is not necessary just normal practice
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")
    # print(help("time"))
    print(time.asctime())
