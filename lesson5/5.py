def summary():
    try:
        with open('lesson55.txt', 'w+') as f:
            line = input('Enter numbers:')
            f.writelines(line)
            numbers = line.split()
            print(sum(map(int, numbers)))
    except ValueError:
        print('It is not nubbers')
    except IOError:
        print('Error')
    finally:
        f.close()

summary()