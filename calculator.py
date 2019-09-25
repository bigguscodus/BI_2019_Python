def div_zero(fst_num, sec_num):
    """Обрабатывает запрос на деление на 0"""
    try:
        return fst_num / sec_num
    except ZeroDivisionError:
        return "Деление на 0 не поддерживается"


def mod_div_zero(fst_num, sec_num):
    """Обрабатывает запрос на деление на 0"""
    try:
        return fst_num % sec_num
    except ZeroDivisionError:
        return "Деление на 0 не поддерживается"


def div_div_zero(fst_num, sec_num):
    """Обрабатывает запрос на деление на 0"""
    try:
        return fst_num // sec_num
    except ZeroDivisionError:
        return "Деление на 0 не поддерживается"


class Calculator():
    def __init__(self, fst_num, sec_num, action):
        self.fst_num = fst_num
        self.sec_num = sec_num
        self.action = action
        self.actions = {'+': self.fst_num + self.sec_num,
                        '-': self.fst_num - self.sec_num,
                        '*': self.fst_num * self.sec_num,
                        'pow': self.fst_num ** self.sec_num,
                        '/': div_zero(self.fst_num, self.sec_num),
                        'mod': mod_div_zero(self.fst_num, self.sec_num),
                        'div': div_div_zero(self.fst_num, self.sec_num)}

    def calculate(self):
        try:
            return self.actions[self.action]
        except KeyError:
            return "Cписок команд: + - * / pow mod div"


first_number = float(input('Введите первое число: '))
action = input('Введите арифметическое действие: ')
second_number = float(input('Введите второе число: '))
cal = Calculator(fst_num=first_number, sec_num=second_number, action=action)
print(cal.calculate())
