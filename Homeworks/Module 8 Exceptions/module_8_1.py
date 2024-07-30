def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, str):
            return f"{a}{b}"
        elif isinstance(a, (str)) and isinstance(b, (int, float)):
            return f"{a}{b}"
        else:
            return a + b
    except TypeError:
        return f"{a} {b}"


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
