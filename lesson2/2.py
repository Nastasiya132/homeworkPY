my_list = []
am_of_elements = int(input('Введите количество элементов которые хотите вывести: '))
i = 0
am = 0
while i < am_of_elements:
    my_list.append(input('Введите данные которые поместите в список: '))
    i += 1
for elements in range(int(len(my_list)/2)):
        my_list[am], my_list[am + 1] = my_list [am + 1], my_list[am]
        am += 2
print(my_list)


