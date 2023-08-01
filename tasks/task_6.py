year: int = int(input("Введите год: "))
month: int = int(input("Введите номер месяца: "))

leap_month: list = [1, 3, 5, 7, 8, 10, 12]
is_leap: bool = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Отлично! Теперь операторы правильно расставлены,
# но есть нюанс, если не обернуть в скобки соответствующую
# пару, программа может выдать неверный результат

if is_leap and month in leap_month:
    print("Да")
else:
    print("Нет")
