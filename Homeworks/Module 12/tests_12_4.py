import unittest
import logging
from rt_with_exceptions import Runner

#logging
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            r1 = Runner('Вася', -5)
            logging.info('OK: test_walk')
        except ValueError as e:
            logging.warning(f'{e} has incorrect speed')

    def test_run(self):
        try:
            r2 = Runner(2)
            logging.info('OK: test_run')
        except TypeError as e:
            logging.warning(f'{e} has incorrect name type')

if __name__ == '__main__':
    unittest.main()