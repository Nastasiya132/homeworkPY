def generator():
    my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    for el in my_list:
        if my_list.count(el) < 2:
            yield el

g = generator()
for i in g:
    print(i)