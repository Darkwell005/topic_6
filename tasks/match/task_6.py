year: int = int(input("Введите год: "))
month: int = int(input("Введите номер месяца: "))

leap_month: list = [1, 3, 5, 7, 8, 10, 12]
is_leap: bool = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

match is_leap, month in leap_month:
    case True, True:
        print("Да")
    case _:
        print("Нет")