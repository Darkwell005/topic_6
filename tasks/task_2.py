nums: int = int(input('Введите целое число: '))

# Можно улучшить код

# 1. Сделать полноценный блок условий, у Вас сейчас получается независимые
# друг от друга блоки if.
# 2. Значения в print() не нужно заключать в кавычки.


if nums > 0:
    print('1')
if nums == 0:
    print('0')
if nums < 0:
    print('-1')

# TODO: Как только исправите, попробуйте решить эту задачу с помощью
#  тернарного оператора (конечно, будет не идеальное решение, но
#  научитесь как его использовать)
