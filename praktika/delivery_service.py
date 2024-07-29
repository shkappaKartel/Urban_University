import cprint


# реализуем модель доставки грузов

# дорога - хранит расстояние между обьектами
# склад - хранит груз и управляет очередями грузовиков
#
# Машина - базовый класс
# имеет
#     кол-во топлива
# может
#     заправляться
#
# Грузовик (Машина)
# имеет
#     ёмкость кузова, скорость движения, расход топлива/час
# может
#     стоять под погрузкой/разгрузкой
#     ехать со скоростью
#
# Погрузчик (Машина)
# имеет
#     скорость погрузки, расход топлива/час
# может
#     загружать/разгружать грузовик
#     ждать грузовик

class Road:

    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Warehouse:

    def __init__(self, name, content=0):
        pass

    def __str__(self):
        pass

    def set_road_out(self, road):
        pass

    def truck_arrived(self, truck):
        pass

    def get_next_truck(self):
        pass

    def truck_ready(self, truck):
        pass

    def act(self):
        pass


class Vehicle:
    fuel_rate = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        pass

    def tank_up(self):
        pass


class Truck(Vehicle):

    def __init__(self, model, body_space=1000):
        pass

    def __str__(self):
        pass

    def ride(self):
        pass

    def go_to(self, road):
        pass

    def act(selfself):
        pass


class AutoLoader(Vehicle):

    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        pass

    def __str__(self):
        pass

    def act(self):
        pass

    def load(self):
        pass

    def unload(self):
        pass


TOTAL_CARGO = 10000

moscow = Warehouse(name= 'Москва', content=TOTAL_CARGO)
piter = Warehouse(name='Питер', content=0)

moscow_piter = Road(start=moscow, end=piter, distance=715)
piter_moscow = Road(start=piter, end=moscow, distance=760)

moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

loader_1 = AutoLoader(model='Bobcat', bucket_capacity=1000, warehouse=moscow, role='loader')
loader_2 = AutoLoader(model='Lonking', bucket_capacity=500, warehouse=piter, role='Unloader')

truck_1 = Truck(model='Камаз', body_space=5000)
truck_2 = Truck(model='ГАЗ', body_space=2000)

moscow.truck_arrived(truck_1)
moscow.truck_arrived(truck_2)

hour = 0
while piter.content < TOTAL_CARGO:
    hour += 1
    cprint('---------------- Час {} ----------------', format(hour), color='red')
    truck_1.act()
    truck_2.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    cprint(truck_1, color='cyan')
    cprint(truck_2, color='cyan')
    cprint(loader_1, color='cyan')
    cprint(loader_2, color='cyan')
    cprint(moscow, color='cyan')
    cprint(piter, color='cyan')


