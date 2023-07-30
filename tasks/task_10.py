ALPHABETS:dict = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")

print("Выберите алфавит:\n1. Латинский\n2. Кириллица")

alphabets: list = [1, 2]
num_alphabets: int = int(input("Введите номер алфавита: "))

if num_alphabets not in alphabets:
    print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
if num_alphabets == 1:
    let = input("Введите букву латинского алфавита: ")
    if let in ALPHABETS["en_vowels"]:
        print(let, "- Гласная буква")
    elif let in ALPHABETS["en_consonants"]:
        print(let, "- Согласная буква")
    else:
        print("Упс! Неизвестная буква. Попробуйте другую!")

else:
    if num_alphabets == 2:
        let = input("Введите букву кириллицы: ")
        if let in ALPHABETS["ru_consonants"]:
            print(let, "- Согласная буква")
        elif let in ALPHABETS["ru_vowels"]:
            print(let, "- Гласная буква")
        else:
            print("Упс! Неизвестная буква. Попробуйте другую!")
