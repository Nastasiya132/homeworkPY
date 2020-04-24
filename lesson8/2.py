class DivisionByZero(Exception):
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def division_by_zero(dividend, divider):
        try:
            return (dividend / divider)
        except:
            return 'И что это мы тут собираемся на нолик делить?!'


division = DivisionByZero(4, 15)
print(DivisionByZero.division_by_zero(2, 0))
print(DivisionByZero.division_by_zero(100500, 0.1))
print(division.division_by_zero(15, 0))