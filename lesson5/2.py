with open('lesson52.txt', 'r') as f:
    print(f.read())
    f.seek(0)
    lines = 0
    letters = 0
    for line in f:
        lines += line.count('\n')
        letters = len(line) - 1
        print(f'The numbers of letters in each line: {letters}')
    print(f'Numbers of lines in a file: {lines}')
f.close()