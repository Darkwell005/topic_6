num: int = int(input("Введите целое число: "))

match num:
    case _ if num < 0:
        print(-1)
    case _ if num > 0:
        print(1)
    case _:
        print(0)

# ---------------------

match [num < 0, num > 0]:
    case [True, False]:
        print(-1)
    case [False, True]:
        print(1)
    case _:  # [False, False]
        print(0)
