with open('lesson53.txt', 'r') as file:
    poor = []
    salary = []
    data = file.read().split('\n')
    for i in data:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        salary.append(i[1])
    print(f'Salary less than 20000: {poor}, average salary: {sum(map(int, salary)) / len(salary)}')