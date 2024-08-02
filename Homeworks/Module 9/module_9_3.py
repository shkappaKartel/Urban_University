def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y

        return add
    elif operation == "substract":
        def substract(x, y):
            return x - y

        return substract
    elif operation == "multiply":
        def multiply(x, y):
            return x * y

        return multiply
    elif operation == "divide":
        def divide(x, y):
            if y == 0:
                return "Error: Division by Zero"
            return x / y

        return divide
    else:
        return None


my_func_add = create_operation("add")
print(my_func_add(1, 2))

my_func_divide = create_operation("divide")
print(my_func_divide(6, 3))
print(my_func_divide(6, 0))

square_lambda = lambda x: x ** 2
print(square_lambda(4))


def square_def(x):
    return x ** 2


print(square_def(4))


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


rectangle = Rect(2, 4)
print(f"Стороны: {rectangle.a}, {rectangle.b}")
print(f"Площадь: {rectangle()}")
