ALPHABETS = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")

print("Выберите алфавит:\n1. Латинский\n2. Кириллица")


num_alphabets = int(input("Введите номер алфавита: "))
if num_alphabets != 1 or 2:
    print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
# I. Обработать самую худшую ситуация первым пункт 1.3
# II. Если все нормально, прошли проверку, то дальше будем работать
#   II.I. Реализуется пункт 1.1, 1.2
#   II.II Реализуется Пункты, 3, 4, 5

elif num_alphabets == 1:
    let = input("Введите букву латинского алфавита: ")
    if let not in ALPHABETS["en_consonants", "en_vowels"]:
        print("Упс! Неизвестная буква. Попробуйте другую!")
    elif let in ALPHABETS["en_vowels"]:
        print(let, "- Гласная буква")
    elif let in ALPHABETS["en_consonants"]:
        print(let, "- Согласная буква")
else:
    if num_alphabets == 2:
        let_2 = input("Введите букву кириллицы: ")
        if let_2 not in ALPHABETS["ru_vowels", "ru_consonants"]:
            print("Упс! Неизвестная буква. Попробуйте другую!")

        elif let_2 in ALPHABETS["ru_vowels"]:
            print(let_2, "- Гласная буква")
        elif let_2 in ALPHABETS["ru_consonants"]:
            print(let_2, "- Согласная буква")
