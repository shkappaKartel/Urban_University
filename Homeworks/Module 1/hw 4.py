immutable_var = 1, True, "Hello", "A"
print(immutable_var)
# immutable_var[0] = 3 :( нельзя изменять элементы картежа

mutable_list = ["mango", "peach", 25, True]
mutable_list[0] = "apple"
mutable_list[1] = 3
mutable_list[2] = False
mutable_list.remove(True)
print(mutable_list)
















# food = ["apple", "coconut", "banana"]
# print(food[0])
# food[0] = "peach"
# print(food)
# food.append(True)
# food.append("mango")
# print(food)
# food.extend("AK")
# food.extend(["AK", 2])
# print(food)
# food.remove("A")
# food.remove("K")
# print(food)
# print("coconut" in food)
# print(food[0:6:2])
# ^^^ ИЗМЕНЯЕМЫЙ ЛИСТ ^^^ больше памяти
# VVV НЕИЗМЕНЯЕМЫЙ КАРТЕЖ VVV меньше памяти
# tuple_ = tuple([1, 2, 3, 4])
# tuple_2 = 5, 6, 7, 8, True, "Hi"

# print(type(tuple_))
# print(tuple_2)
# print(tuple_[0])
