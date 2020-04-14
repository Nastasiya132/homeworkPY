data = []
while True:
    line = input("Enter anything: ")
    if line == '':
        print(data)
        exit()
    else:
        new_line = line + '\n'
        data.append(new_line)

    with open('lesson51.txt', 'w') as file:
        file.writelines(data)
    file.close()