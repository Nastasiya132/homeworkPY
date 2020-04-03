a = int(input('Введите число: '))
max_a = a % 10
a = a // 10
while a > 0:
    if a % 10 > max_a:
        max_a = a % 10
    a = a // 10
print(max_a)