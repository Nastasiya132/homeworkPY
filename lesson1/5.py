revenue = int(input('Введите вашу выручку в рублях: '))
costs = int(input('Введите ваши издержки в рублях: '))

if  revenue > costs:
     print('Поздравляю! Вы в плюсе) А сейчас я посчитаю Вашу рентабельность, смотрите ниже')
     profitability: int = revenue - costs
     print (f' Ваша рентабельность: {profitability} рублей')
     staff = int(input('Введите численность Ваших сотрудников: '))
     revenue_pers: int = profitability / staff
     print(f'С учетом Вашего штата выручка на одного сотрудника составляет: {revenue_pers:.2f} рублей')
elif revenue == costs:
    print("Ваша компания работает в ноль, думаю Вам слегка стоит пересмотреть стратегию")
else:
    print('Вам нужно срочно пересмотреть стратегию Вашего бизнеса, так как вы работаете в убыток!')
