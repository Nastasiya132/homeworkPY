def summa():
    sum_result = 0
    ex = False
    while ex == False:
        entered_number = input('Нажмите - Q, что бы выйти или введите числа через пробел: ').split()
        result = 0
        for elements in range(len(entered_number)):
            if entered_number[elements] == 'q' or entered_number[elements] == 'Q':
                ex = True
                break
            else:
                result = result + int(entered_number[elements])
        sum_result = sum_result + result
        print(f'Промежуточный результат - {sum_result}')
    print(f'Сумма всех сложений - {sum_result}')

summa()