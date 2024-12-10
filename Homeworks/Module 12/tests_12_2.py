# -*- coding: utf8 -*-

import unittest
from unittest import TestCase

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        cls = self.__class__
        if getattr(cls, "is_frozen", False):
            raise unittest.SkipTest("Тесты заморожены")
        return test_func(self, *args, **kwargs)
    return wrapper


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        # Словарь для хранения результатов
        cls.all_results = {}

    def setUp(self):
        # Создаем бегунов с разной скоростью
        self.usain = Runner(name="Усэйн", speed=10)
        self.andrei = Runner(name="Андрей", speed=9)
        self.nick = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        # Вывод результатов всех тестов
        for key, result in cls.all_results.items():
            formatted_result = {place: str(runner) for place, runner in result.items()}
            print(formatted_result)

    @skip_if_frozen
    def test_aRace(self):
        # ||| Усэйн - Ник | 90метров |||
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        # сохранение результата
        self.__class__.all_results[1] = results
        # проверка, что Ник последний
        self.assertTrue(results[max(results.keys())] == "Ник")

    @skip_if_frozen
    def test_bRace(self):
        # ||| Андрей - Ник | 90метров |||
        tournament = Tournament(90, self.andrei, self.nick)
        results = tournament.start()
        self.__class__.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @skip_if_frozen
    def test_trioRace(self):
        # ||| Усэйн - Андрей - Ник | 90метров |||
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        results = tournament.start()
        self.__class__.all_results[3] = results
        self.assertTrue(results[max(results.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()