whole_num: int = int(input('Введите целое число: '))
fractional_num: float = float(input('Введите дробное число: '))
line: str = input('Введите строку: ')

mixed: list = [whole_num, fractional_num, line]

match all(mixed):
    case True:
        print('Да')
    case _:
        print('Нет')
