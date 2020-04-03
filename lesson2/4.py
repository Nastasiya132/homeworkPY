string_of_words = input('Введите несколько слова через пробел: ')
entered_words = string_of_words.split(' ')
for ind, el in enumerate(entered_words, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{ind}. {el}")