year = int(input("Введите год: "))
month = int(input("Введите номер месяца: "))

leap_month = [1, 3, 5, 7, 8, 10, 12]


is_leap: bool = year % 4 == 0 or year % 100 != 0 or year % 400 == 0
if is_leap:
    if month not in leap_month:
        print("Нет")
    if month in leap_month:
        print("Да")

