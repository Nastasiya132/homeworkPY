my_dict = {}
with open('lesson56.txt', 'r') as f:
    for line in f:
        subject, lectures, practices, laboratory = line.split()
        my_dict[subject] = int(lectures) + int(practices) + int(laboratory)
    print(f'Total hourse in subjects: {my_dict}')
f.close()
