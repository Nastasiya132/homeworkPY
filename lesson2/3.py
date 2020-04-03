seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
mounth = int(input('Введите номер месяца по счету согласно календарю: '))
if mounth == 1 or mounth == 2 or mounth == 12:
    print(seasons_dict.get(1))

elif mounth == 3 or mounth == 4 or mounth == 5:
    print(seasons_dict.get(2))

elif mounth == 6 or mounth == 7 or mounth == 8:
    print(seasons_dict.get(3))

elif mounth == 9 or mounth == 10 or mounth == 11:
    print(seasons_dict.get(4))
else:
    print("Вы ввели цифру не соответствующую ни одному месяцу в году")


seasons_list = ['winter','spring', 'summer', 'autumn']
mounth = int(input('Введите номер месяца по счету согласно календарю: '))
if mounth == 1 or mounth == 2 or mounth == 12:
    print(seasons_list[0])

elif mounth == 3 or mounth == 4 or mounth == 5:
    print(seasons_list[1])

elif mounth == 6 or mounth == 7 or mounth == 8:
    print(seasons_list[2])

elif mounth == 9 or mounth == 10 or mounth == 11:
    print(seasons_list[3])
else:
    print("Вы ввели цифру не соответствующую ни одному месяцу в году")