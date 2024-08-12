# -*- coding: utf8 -*-

import threading
import time


def print_nums():
    for i in range (1, 11):
        print(i)
        time.sleep(1)


def print_letters():
    for letter in 'abcdefghij':
        print(letter)
        time.sleep(1)


thread1 = threading.Thread(target=print_nums, name='NumbersThread')
thread2 = threading.Thread(target=print_letters, name='LettersThread')

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Оба потока выполнили свою работу")


def write_words(word_counter, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_counter + 1):
            file.write(f'Слово № {i}\n')
            time.sleep(0.1)
    print(f'Запись в файл {file_name} завершена')


start_time = time.time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end_time = time.time()

print(f'Работа выполнения всех функций заняла {end_time - start_time} секунд')

start_time_threads = time.time()

thread1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
thread2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
thread3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
thread4 = threading.Thread(target=write_words, args=(100, "example8.txt"))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time_threads = time.time()

print(f'Работа поттопк заняла {end_time_threads - start_time_threads} секунд.')


'''
Для удобства проверки задания дублирую вывод из консоли

1
a
b
2
3
c
d
4
5
e
f
6
7
g
h
8
9
i
j
10
Оба потока выполнили свою работу
Запись в файл example1.txt завершена
Запись в файл example2.txt завершена
Запись в файл example3.txt завершена
Запись в файл example4.txt завершена
Работа выполнения всех функций заняла 34.127708435058594 секунд
Запись в файл example5.txt завершена
Запись в файл example6.txt завершена
Запись в файл example8.txt завершена
Запись в файл example7.txt завершена
Работа поттопк заняла 20.090641260147095 секунд.
'''