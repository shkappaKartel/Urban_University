def test1():
    a = 5
    b = 10
    print(a, b)


test1()


def test2(a, b, *, c):
    print(a, b, c)


test2(1, 2, c=3)
