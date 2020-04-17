from itertools import count, cycle

for i in count(2, 3):
    print(i)
    if i > 45:
        break

for i, words in enumerate(cycle(['stop', 'go', 'wait']), 1):
    print(i, words)
    if i > 30:
        break