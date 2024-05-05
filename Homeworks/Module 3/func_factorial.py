def test(*params):
    for param in params:
        print(param)


def get_factorial(n):
    if n == 0:
        return 1
    else:
        return n * get_factorial(n - 1)


test(1, "stRRRing", [1, 2, 1], {'a': 67, 'b': 21, 'c': "STrrrING"})

n = int(input('Введите число, факториал которого хотите посчитать'))
print(f"Факториал числа {n} равен:", get_factorial(n))
