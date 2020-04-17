my_list = [10, 100, 1200, 40, 20, 6, 70, 99]
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num] ]
print(f'Initial sheet : {my_list}')
print(f'Sorted sheet: {new_list}')