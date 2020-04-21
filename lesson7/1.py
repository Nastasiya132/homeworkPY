class Matrix:
    def __init__(self, my_list1, my_list2):
        self.my_list1 = my_list1
        self.my_list2 = my_list2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        for i in range(len(self.my_list1)):

            for j in range(len(self.my_list2[i])):
                matr[i][j] = self.my_list1[i][j] + self.my_list2[i][j]
        return str('\n' + '\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.my_list1])) + '\n' + '\n' + str(
            '\n'.join(['\t'.join([str(j) for j in i]) for i in self.my_list2]))


my_matrix = Matrix([[-1, 20, 10],
                    [26, 7, 24],
                    [13, 25, 85]],
                   [[88, -6, 13],
                    [14, 10, 2],
                    [32, 4, 100]])

print(my_matrix)
print(f'\nРезультат сложения двух матриц:{my_matrix.__add__()}')
