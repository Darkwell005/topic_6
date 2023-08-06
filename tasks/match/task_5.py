num: int = int(input("Введите целое число: "))

match num:
    case _ if num % 2 == 0:
        print("Число", num, "является четным")
    case _:
        if num % 2 != 0 and num * 3 > 20:
            print("Результат умножения", num,  "на 3 больше 20")
        else:
            print("Число", num,  "не соответствует условиям")
