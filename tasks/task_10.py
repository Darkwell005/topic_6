ALPHABETS: dict = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")

print("Выберите алфавит:\n1. Латинский\n2. Кириллица")

alphabets: list = [1, 2]
num_alphabets: int = int(input("Введите номер алфавита: "))

if num_alphabets not in alphabets:  # Отлично!
    print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
if num_alphabets == 1:  # А вот тут беда. Что если, выбран неверный алфавит,
    # верхний if выведет сообщение об ошибке, а этот блок условий в любом
    # случае будет проверяется, разве это логично?
    let = input("Введите букву латинского алфавита: ")
    if let in ALPHABETS["en_vowels"]:
        print(let, "- Гласная буква")
    elif let in ALPHABETS["en_consonants"]:
        print(let, "- Согласная буква")
    else:
        print("Упс! Неизвестная буква. Попробуйте другую!")

else:
    if num_alphabets == 2:  # Это лишняя проверка, если num_alphabets == 1
        # ложно то в любом случае это 2, опять это будет правильно,
        # после того, как исправите замечание выше
        let = input("Введите букву кириллицы: ")
        if let in ALPHABETS["ru_consonants"]:
            print(let, "- Согласная буква")
        elif let in ALPHABETS["ru_vowels"]:
            print(let, "- Гласная буква")
        else:  # одно и тоже повторяется, смотрите на строку 26
            print("Упс! Неизвестная буква. Попробуйте другую!")

#  В целом у Вас хорошая реализация, необходимо немного улучшить
