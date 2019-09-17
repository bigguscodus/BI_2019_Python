def division_zero(first_number, second_number):
    """Обрабатывает запрос на деление на 0"""
    try:
        return first_number / second_number
    except ZeroDivisionError:
        return "Деление на 0 не поддерживается"


def mod_division_zero(first_number, second_number):
    """Обрабатывает запрос на деление на 0"""
    try:
        return first_number % second_number
    except ZeroDivisionError:
        return "Деление на 0 не поддерживается"


def div_division_zero(first_number, second_number):
    """Обрабатывает запрос на деление на 0"""
    try:
        return first_number // second_number
    except ZeroDivisionError:
        return "Деление на 0 не поддерживается"


class Calculator():
    def __init__(self, first_number, second_number, action):
        self.first_number = first_number
        self.second_number = second_number
        self.action = action
        self.actions = {'+': self.first_number + self.second_number, '-': self.first_number - self.second_number,
                        '*': self.first_number * self.second_number, 'pow': self.first_number ** self.second_number,
                        '/': division_zero(self.first_number, self.second_number),
                        'mod': mod_division_zero(self.first_number, self.second_number),
                        'div': div_division_zero(self.first_number, self.second_number)}

    def calculate(self):
        try:
            return self.actions[self.action]
        except KeyError:
            return "Cписок команд, поддерживаемых калькулятором c числами: + - * / pow mod div"


first_number = float(input('Введите первое число: '))
action = input('Введите арифметическое действие: ')
second_number = float(input('Введите второе число: '))
calculator = Calculator(first_number=first_number, second_number=second_number, action=action)
print(calculator.calculate())
