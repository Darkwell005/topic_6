num_1: int = int(input('Введите первое целое число: '))
num_2: int = int(input('Введите второе целое число: '))
num_3: int = int(input('Введите третье целое число: '))
all_num = [num_1, num_2, num_3]
text: str = 'Наибольшее число:'
match all_num:
    case _ if num_1 > num_2 and num_1 > num_3:
        print(text, num_1)
    case _ if num_2 > num_1 and num_2 > num_3:
        print(text, num_2)
    case _:
        print(text, num_3)
