name_pit: str = input("Введите имя своего питомца: ")

match name_pit:
    case "Барсик" | "Мурка":
        print("У вас классное имя для питомца!")
    case _:
        print("Это тоже хорошее имя для питомца!")