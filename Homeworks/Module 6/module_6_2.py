class Vehicle:
    def __init__(self):
        self.vehicle_type = 'none'


class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return 149


class Nissan(Car, Vehicle):
    def __init__(self):
        Car.__init__(self)
        Vehicle.__init__(self)
        self.price = 12000000
        self.vehicle_type = "car"


nissan_car = Nissan()

print(f'Your {nissan_car.vehicle_type} done completefuly!')
print(f'Price: {nissan_car.price}')