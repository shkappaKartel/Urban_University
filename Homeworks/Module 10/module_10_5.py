# -*- coding: utf-8 -*-

import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open (name, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

filenames = [f'./10_5/file {number}.txt' for number in range(1, 5)]

def linear():
    start_time = time.time()

    for filename in filenames:
        read_info(filename)

    end_time = time.time()
    print(f'Линейный вызов выполнил работу за: {end_time - start_time} секунд')

def multiprocessing():
    start_time = time.time()

    with Pool() as pool:
        pool.map(read_info, filenames)

    end_time = time.time()
    print(f'Многопроцессорный вызов выполнил работу за: {end_time - start_time} секунд')

if __name__ == '__main__':
    linear()
    multiprocessing()