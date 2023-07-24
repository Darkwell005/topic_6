whole_num = int(input('Введите целое число: '))
fractional_num = float(input('Введите дробное число: '))
line = input('Введите строку: ')

mixed = [whole_num, fractional_num, line]
if all(mixed):
    print('Да')
else:
    print('Нет')

# Отлично! Добавьте пожалуйста аннотации типа ко всем переменным
