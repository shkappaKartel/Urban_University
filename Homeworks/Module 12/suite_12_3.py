import unittest
from module_12_1 import RunnerTest
from tests_12_2 import TournamentTest

runnerTS = unittest.TestSuite()
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test=runnerTS)