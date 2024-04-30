x = 38

print('Привет')
if x < 0:
    print('Меньше неля')
print('Пока')


a, b = 10, 5

if a < b:
    print('a > b')

if a > b and a > 0:
    print('Done1!')

if (a > b) and (a > 0 or b < 1000):
    print('Done2!')

if 5 < b < 10:
    print('Done3')


if '34' > '123':
    print('Done 1')

if '123' > '12':
    print('Done 2')

if [1, 2] > [1, 1]:
    print('Done 3')

if '6' != 5:
    print('Done 1')