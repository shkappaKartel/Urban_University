# -*- coding: utf8 -*-

import random
import threading
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.locked = False

    def deposit(self):
        for _ in range(100):
            income = random.randint(50, 500)
            with self.lock:
                self.balance += income
                print(f"Пополнение: {income}. Баланс: {self.balance}")
                if self.balance >= 500 and self.locked:
                    self.lock.release()
                    self.locked = False
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            withdraw = random.randint(50, 500)
            print(f"Запрос на {withdraw}")
            with self.lock:
                if withdraw <= self.balance:
                    self.balance -= withdraw
                    print(f"Снятие: {withdraw}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    if not self.locked:
                        self.lock.acquire()
                        self.locked = True
            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
thread1 = threading.Thread(target=Bank.deposit, args=(bk,))
thread2 = threading.Thread(target=Bank.take, args=(bk,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Итоговый баланс: {bk.balance}')
