def sum_three(a, b, c):
    return a + b + c


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, int(result**0.5)+1):
                if not result % i:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result
    return wrapper


@is_prime
def sum_three_decorated(a, b, c):
    return sum_three(a, b, c)


result = sum_three_decorated(2, 3, 6)
print(result)
