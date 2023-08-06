ALPHABETS: dict = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")
print("Выберите алфавит:\n1. Латинский\n2. Кириллица\n")

alphabets: list = [1, 2]
num_alphabets: int = int(input("Введите номер алфавита: "))

match num_alphabets in alphabets:
    case True:
        match num_alphabets:
            case 1:
                pass
            case 2:
                pass
            # TODO: Проблема: Как не дублировать код для каждого алфавита.
    case _:
        print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
