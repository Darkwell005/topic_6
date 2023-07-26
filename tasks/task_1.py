name_animal: str = input('Введите имя своего питомца: ')

name_animal: str = ('Это тоже хорошее имя для питомца!'
                    if name_animal != 'Мурка' and name_animal != 'Барсик'
                    else 'У вас классное имя для питомца!')
print(name_animal)
