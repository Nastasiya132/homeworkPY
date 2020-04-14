russian_leng = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_lesson54 = []
with open('lesson54.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        new_lesson54.append(russian_leng[i[0]] + ' ' + i[1])
    print(new_lesson54)

with open('lesson54_new.txt', 'w') as file:
    file.writelines(new_lesson54)
file.close()