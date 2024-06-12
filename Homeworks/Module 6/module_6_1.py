class Car:
    price = 1000000
    horse_powers = 149


class Nissan(Car):
    price = 1800000
    horse_powers = 280


class Kia(Car):
    price = 1200000
    horse_powers = 121


print(Car.price)
print(Car.horse_powers)
print(Nissan.price)
print(Nissan.horse_powers)
print(Kia.price)
print(Kia.horse_powers)
