def print_params(a=1, b="two", c=True):
    print(a, b, c)


print_params()
print_params(4, "otw", False)
print_params(3)
# print_params(4, "too many", True, 5) too many parameters
# print_params(b=25) -- incorrect type (str) expected. got (int)
# print_params(c=[1,2,3]) -- incorrect type (list) -- (bool)

values_list = [51, "string", False]
values_dict = {'a': 78, 'b': "newString", 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, True]
print_params(*values_list_2)

