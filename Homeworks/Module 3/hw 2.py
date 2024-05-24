# m3hw2
def print_params(a=1, b='stroka', c=True):
    print(a, b, c)
    # print(f"a: {a}, b: {b}, c: {c}")


print_params()

print_params(10)

print_params(10, 'pomenyalos')

print_params(10, 'eshe raz', False)

values_list = [42, 'string', False]
values_dict = {'a': 90, 'b': 'bstring', 'c': [4, 5, 6]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [100, 'vlstring2']
print_params(*values_list_2)
print_params(*values_list_2, 525)
