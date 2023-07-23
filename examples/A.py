petya = int(input())
vasya = int(input())
tolya = int(input())

first = ''
second = ''
third = ''

if petya > vasya and petya > tolya:
    first = 'Петя'
    if vasya > tolya:
        second = 'Вася'
        third = 'Толя'
    else:
        second = 'Толя'
        third = 'Вася'
elif vasya > petya and vasya > tolya:
    first = 'Вася'
    if petya > tolya:
        second = 'Петя'
        third = 'Толя'
    else:
        second = 'Толя'
        third = 'Петя'
else:
    first = 'Толя'
    if petya > vasya:
        second = 'Петя'
        third = 'Вася'
    else:
        second = 'Вася'
        third = 'Петя'


print('1. ' + first, '2. ' + second, '3. ' + third, sep='\n')

# https://new.contest.yandex.ru/41234/problem?id=149944/2022_10_12/zai536kBZM

# ----------------------- pass

# a = 4
# b = 6
#
# if a > b:
#     pass
# else:
#     print('Hello, World')

