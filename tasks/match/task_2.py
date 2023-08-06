num: int = int(input("Введите целое число: "))

match num:
    case _ if num < 0:
        print(-1)
    case _ if num > 0:
        print(1)
    case _:
        print(0)
