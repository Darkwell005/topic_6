num_whole: int = int(input('Введите целое число: '))
num_fractional: float = float(input('Введите дробное число: '))
line: str = input('Введите строку: ')

mixed = [num_fractional, num_whole, line]
if any(mixed):
    print('Да')
else:
    print('Нет')

# Отлично! Добавьте пожалуйста аннотации типа ко всем переменным
