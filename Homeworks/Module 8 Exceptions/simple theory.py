print('----------------------------------------------------')
print('Простая теория для работы с try и except')
print('----------------------------------------------------')
print('')

print('100 / x')
i = int(input('x = '))

try:
    result = 0
    result = 100 / i
except ZeroDivisionError as exc:
    print('На ноль делить нельзя')
else:
    print('Делим...')
finally:
    # добавляю if чтобы не выскакивала ошибка result not defined
    if result:
        print(f'Результат = {int(result)}')
    else:
        print('Заканчиваю работу.')
