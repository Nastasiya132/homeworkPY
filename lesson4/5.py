from functools import reduce

def generator():
    for el in range(99, 1001):
        if el % 2 == 0:
            yield el
g = generator()
for i in g:
    print(i)

def my_func(a, b):
    return a + b

print(reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0]))

# Одного не поняла: реальзовать список- это list или что бы списком длинным выдавалось