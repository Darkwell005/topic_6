num_1: float = float(input('Введите первое число: '))
num_2: float = float(input('Введите второе число: '))
operation: str = input('Введите магическую операцию: ')
operations: list = ["Призыв",
                    "Трансформация",
                    "Объединение",
                    "Исчезновение"]

if operation == operations[0]:
    print("Сумма магических сил чисел:", num_1 + num_2)
elif operation == operations[1]:
    # Работает некорректно, также отсутствует текст вывода
    print(abs(num_1) - abs(num_2))
elif operation == operations[2]:
    print('Объединение чисел:', num_1 * num_2)
elif operation == operations[3]:
    if num_2 == 0:
        print('Ошибка: Второе число равно нулю!')
    if num_2 != 0:
        # Неправильно работает операция "Исчезновение"
        print('Исчезновение числа:', num_1 - num_1)
else:
    print('Ошибка: Некорректная операция')

# В целом все хорошо, исправьте ошибки. Также добавьте пожалуйста аннотации.
