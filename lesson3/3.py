def my_func(x, y):
    return x ** y
print(my_func(2, -6))



def my_func_cik(x, y):
    if y == 0:
        return 0
    elif y == 0:
        return 1
    elif y == 1:
        return x
    elif y < 0:
        return 1 / (x * my_func_cik(x, -y - 1))
    else:
        return x * my_func_cik(x, y - 1)

print(my_func_cik(2, -6))