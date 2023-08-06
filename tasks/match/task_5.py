num: int = int(input("Введите целое число: "))

match num:
    case _ if num % 2 == 0:
        print("Число", num, "является четным")
    case _ if num * 3 > 20:
        print("Результат умножения", num, "на 3 больше 20")
    case _:
        print("Число", num, "не соответствует условиям")

# ---------------------

condition: list = [
    num % 2 == 0,
    num * 3 > 20
]

match condition:
    case [True, False]:
        print("Число", num, "является четным")
    case [False, True]:
        print("Результат умножения", num, "на 3 больше 20")
    case _:
        print("Число", num, "не соответствует условиям")
