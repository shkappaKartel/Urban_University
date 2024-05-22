def generate_password(n):
    pairs = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if (i + j) % n == 0:
                pairs += str(i) + str(j)
    return pairs


# БЫСТРАЯ ПРОВЕРКА ГЕНЕРАТОРА
for num in range(3, 21):
    print(num, "-", generate_password(num))

num = input('Введите число, которое выпадет в первой ячейке (3-20) >>> ')
num = int(num)

if num < 3 or num > 20:
    print('Ошибка! 0_o Введите число от 1 до 20')

if 3 <= num <= 20:
    print(f'[{num}] - [{generate_password(num)}]')


