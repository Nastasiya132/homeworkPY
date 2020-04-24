class NumbError(Exception):
    def __init__(self, *numbs):
        self.my_list = []

    def input_list(self):
        while True:
            try:
                value_list = int(input('Entered number: '))
                self.my_list.append(value_list)
                print(self.my_list)
            except:
                print('Wrong!')
                quit_func = input('You wanna more? Y/N: ')

                if quit_func == 'Y' or quit_func =='y':
                  print(self.input_list())
                elif quit_func == 'N' or quit_func == 'n':
                    return 'Quit'
                else:
                    return 'Quit'


numbers = NumbError(5)
print(numbers.input_list())

