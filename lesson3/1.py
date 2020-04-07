def division(*args):

    try:
        dividend = int(input('Введите число (делимое): '))
        divider = int(input('Введите число (делитель): '))
        result = dividend / divider
        return result
    except ValueError:
        return 'Вы ввели не число, а что-то инопланетное'
    except ZeroDivisionError:
        return 'И что это мы тут собираемся на нолик делить?!'

print(division())

#у меня не получилось найти другое решение, программа постоянно ругается на ZeroDivisionError


# def division(*args):
#     result = dividend / divider
#     if divider != 0:
#         return result
#     else:
#         return 'ну и что мы тут всякие глупости вводим?!'
#
# dividend = int(input('Введите число (делимое): '))
# divider = int(input('Введите число (делитель): '))
# print(division())

# def division(*args):
#     result = dividend / divider
#     if divider == 0:
#         return 'ну и что мы тут всякие глупости вводим?!'
#     else:
#         return result
#
# dividend = int(input('Введите число (делимое): '))
# divider = int(input('Введите число (делитель): '))
# print(division())