# -*- coding: utf8 -*-

import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days = 0
        print(f'{self.name}, на нас напали!')

        while enemies > 0:
            time.sleep(1)
            days += 1
            enemies -= self.power
            enemies = max(0, enemies)
            print(f'{self.name}, сражается {days} дней. Осталось {enemies} врагов')

        print(f'{self.name} одержал победу спустя {days} дней')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы были закончены')


