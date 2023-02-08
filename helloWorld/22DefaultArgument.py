# default ,  arguments  ,exercise
import time


# ---- EXAMPLE ----
def net_price(list_price, discount=0, tax=0.05):
    print(list_price)
    print(discount)
    print(tax)
    return list_price * (1 - discount) * (1 - tax)


# print(net_price(500))
# print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))

# ---- EXERCISE ----
# import time

print(f"sleep game")


def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")


count(10)
# count(30, 15)
