color: str = input("Введите ваш любимый цвет: ")

match color:
    case "солнечно-желтый" | "небесно-голубой":
        print("Это цвет радости и счастья!")
    case _:
        print("Это тоже хороший цвет!")
