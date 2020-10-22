import unittest
import DigitalSolver


class DigitalSolverUnitTest(unittest.TestCase):
    def test_digital_root(self):
        self.assertEqual(DigitalSolver.digital_root(493193), 2)

    def test_find_outliner(self):
        self.assertEqual(DigitalSolver.find_outlier([2, 3, 4, 6, 12]), 3)


if __name__ == '__main__':
    unittest.main()
