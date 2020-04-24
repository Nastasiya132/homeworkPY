class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extraction(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    def __str__(self):
        return f'The current date {Data.extraction(self.day_month_year)}'

    @staticmethod
    def validation(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'all right'
                else:
                    return 'wrong year'
            else:
                return 'wrong month'
        else:
            return 'wrong day'


today = Data('23 - 04 - 2020')
print(today)
print(Data.validation(12, 10, 2345))
print(today.validation(23, 0, 2020))
print(today.extraction('21 - 04 - 2021'))
print(Data.validation(2, 9, 1991))
