# -*- coding: utf8 -*-

import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest (unittest.TestCase):
    def test_walk(self):
        runner = Runner('Bob')
        for step in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('John')
        for step in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_1 = Runner('T3X4')
        runner_2 = Runner('KRL15')
        for step in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance, 'дистанцая разная')

if __name__ == '__main__':
    unittest.main()