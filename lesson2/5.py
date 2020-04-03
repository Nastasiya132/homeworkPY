entered_number = int(input('Введите число: '))
my_list = [7 , 5 , 3 , 1]
a = my_list.count(entered_number)
for el in my_list:
    if a > 0:
        i = my_list.index(entered_number)
        my_list.insert(i + a, entered_number)
        break
    else:
        if entered_number > el:
            b = my_list.index(el)
            my_list.insert(b, entered_number)
            break
        elif entered_number < my_list[len(my_list) -1]:
            my_list.append(entered_number)
print(my_list)