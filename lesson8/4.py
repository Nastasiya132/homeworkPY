class Stock:
    def __init__(self, *args):
        self.stock_all = []
        self.stock = []


class OfficeEquipment:
    def __init__(self, name, article, price, quantity, *args):
        self.name = name
        self.article = article
        self.price = price
        self.quantity = quantity
        self.stock_dict = {'Наименование': self.name, 'Артикл устройства': self.article, 'Цена': self.price,
                           'Остаток на складе': self.quantity}
        self.stock_all = []
        self.stock = []

    def __str__(self):
        return f'{self.name} - стоимость: {self.price}, остаток на складе: {self.quantity}'

    def formation(self):
        try:
            entered_name = input('Введите наименование: ')
            entered_article = input('Ввкдите артикл товара: ')
            entered_price = input('Введите цену товара: ')
            entered_quantity = input('Введите кол-во: ')
            dict_oe = {'Наименование': entered_name, 'Артикл устройства': entered_article, 'Цена': entered_price,
                       'Остаток на складе': entered_quantity}
            self.stock_dict.update(dict_oe)
            self.stock.append(self.stock_dict)
            print(f'{self.stock}')
        except:
            return f'Wrong'

        print(f'For exit tab Q, more? tab Enter')
        q = input()
        if q == 'Q' or q == 'q':
            self.stock_all.append(self.stock)
            print(f'All Stock: {self.stock_all}')
            return f'Exit'
        else:
            return OfficeEquipment.formation(self)


class Printer(OfficeEquipment):

    def print_func(self):
        return f'Принтеры на складе только с лазерной печатью'


class Scanner(OfficeEquipment):
    def scan_func(self):
        return f'Сканеры на складе только тонкие'


class Copier(OfficeEquipment):
    def cop_func(self):
        return 'Копировальные аппараты на складе только для офисов'


product_1 = Printer('Canon', 'AP1500', 7000, 4)
product_2 = Scanner('Canon', 'AS7500', 3000, 15)
product_3 = Copier('HP', 'H7500', 45000, 5)
print(product_1.formation())
print(product_2.formation())
print(product_3.formation())
print(product_1.print_func())
print(product_2.scan_func())
print(product_3.cop_func())