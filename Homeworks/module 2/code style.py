# -*- coding: utf-8 -*-

# Блоки кода

x, y = -10, 29

if x < 0:
    print('Х меньше нуля')
    z = x ** 2 + y
else:
    print('Х больше нуля')
    z = x - y
print('Результат', z)

# Ср. с С++

# if (x < 0) {
#   printf('Меньше нуля\n');
#   z = x**2 + y; }
# else {\
#   printf('Больше нуля\n');
#   z = x - y; }
# printf('Получается\n', z)

# Вложенные блоки кода

name = input('Enter your name >>> ')
if name == 'Ola':
    opponent = 'Ola'
    print('Hi, Ola!')
else:
    if name == 'Sofi':
        opponent = 'Sofi'
        print('Hi, Sofi!')
    else:
        if name == 'Katy':
            opponent = 'Katy'
            print('Hi, Katy!')
        else:
            opponent = str(name)
            print(f'Hi, {opponent}!')

# Оператор pass

if x < 0:
    if y > 0:
        z = -x + y
    else:
        z = -x - y
else:
    z = x + y

# Соглашения о стиле кода
# PEP8 (Python Enhancement Proposal 8) - описан "правильный" стиль программирования в Питоне
# https://www.python.org/dev/peps/pep-0008/

# 4 пробела на каждый уровень отступа

if x < 0:
    if y > 0:
        pass
    else:
        print('направо!')
else:
    print('стой!')

# Максимальная длина строки

my_poem = ['Варкалось, хливкие шорьки пырялись по наве',
           'И хрюкотали зелюки как мюмзики в мове',
           'О бойся Бармаглота, сын! Он так свирлеп и дик',
           'А в глуше рымит исполин - Злопастный Брандашмыг!']

# Пробелы в операторах

x = 2
y = x * x + 1
is_big = x >= 3000

x = my_poem[-1]
print(x)
my_list = [2, 3, 4, 5, 6]

# Reformat кода

x, v = -43, 8

if x == 3:
    print(42)

if x < 0:
    if v > 0:
        print('налево!')
    else:
        print('направо!')
else:
    print('стой!')

# Названия переменных

pets_count = 34
if pets_count > 10:
    print('I need more space for my pets!')

favor_pets = ['cat', 'wolf', 'ostrich']
if 'lion' in favor_pets:
    print('Wow!')

favor_pets = ['cat', 'wolf', 'ostrich']
# Но такой стиль используется для названий классов

# Рекомендации PEP8

# b (одиночная маленькая буква)
# B (одиночная заглавная буква)
# Но лучше использовать только такие однобуквенные имена:
#   i j k - для циклов
#   x y z - для координат

# Никогда не используйте в названиях переменных одиночные l, I, O!

num1 = 34
num2 = 43
if num1 > num2:
    print()
num0 = 9
if num0 > 0:
    print()

# lowercase (слово в нижнем регистре)
# lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
# UPPERCASE (заглавные буквы)
# UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)

# CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase).
#   Замечание: когда вы используете аббревиатуры в таком стиле, пишите все буквы аббревиатуры заглавными —
#   HTTPServerError лучше, чем HttpServerError.

# mixedCase (отличается от CapitalizedWords тем, что первое слово начинается с маленькой буквы)
# Capitalized_Words_With_Underscores (слова с заглавными буквами и подчеркиваниями — уродливо!)

# Автоматическое переименование в PyCharm и подсказки - вам не нужно набирать длинные названия переменных

my_pets = ['cat', 'wolf', 'ostrich']
if 'lion' in my_pets:
    print('Wow!')
