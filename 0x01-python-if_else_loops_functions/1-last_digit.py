#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = int(repr(number)[-1])
if number < 0:
    ld = -ld
print("Last digit of {} is {} and is ".format(number, ld), end="")

if ld == 0:
    print("0")
elif ld > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
