def salary():
    try:
        time_work =  int(input('Введите сколько часов отработал Ваш сотрудник: '))
        salaty_in_hours = int(input('Введите сколько Ваш сотрудник получает в час: '))
        kpi = int(input('Какая премия у Вашего сотрудника: '))
        sum_salary = time_work * salaty_in_hours + kpi
        return f'Итого : {sum_salary}'
    except ValueError:
        return 'Вы ввели что-то не то...'

print(salary())

