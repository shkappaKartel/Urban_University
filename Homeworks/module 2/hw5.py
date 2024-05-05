def test():
    a = 5
    b = 10
    print(a, b)

test()


def test(a, b,*, c):
    print(a, b, c)

test(1, 2, c = 3)