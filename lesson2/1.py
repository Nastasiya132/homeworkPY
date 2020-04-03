my_dict = { 'planet': 'Earth', 'population': 7530000000000, 'rationality': 'controversial'}
my_tuple = ('home', 'war', 12)
my_list = ['history', 1045, 1.5, my_dict, my_tuple]
for i in my_list:
    print(f'{i} is {type(i)}')