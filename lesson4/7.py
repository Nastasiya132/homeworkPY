from math import factorial
from itertools import count

def fact():
    for el in count(1):
            yield factorial(el)
x = 1
for i in fact():
    if x < 10:
        print(i)
        x += 1
    else:
        break