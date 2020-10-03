import main
import unittest
import random


class Test(unittest.TestCase):

    # test the value with correct expected output
    def testStartSmallerThanEnd(self):
        print("testStartSmallerThanEnd")
        self.assertEqual(main.printRange(0, 2, 1), [0, 1])
        print("testStartSmallerThanEnd successful")

    # test the value with start higher than end
    def testEndSmallerThanStart(self):
        print("testEndSmallerThanStart")
        self.assertRaises(ValueError, main.printRange(2, 0, 1))

    # test the value with step set to zero
    def testEndStepToZero(self):
        print("testEndStepToZero")
        self.assertRaises(ValueError, main.printRange(0, 2, 0))

    # test the value with negative step
    def testEndStepNegative(self):
        print("testEndStepNegative")
        self.assertRaises(ValueError, main.printRange(2, 0, -1))

    # test the value with all set to zero 
    def testEndAllSetToZero(self):
        print("testEndAllSetToZero")
        self.assertRaises(ValueError, main.printRange(0, 0, 0))


if __name__ == '__main__':
    unittest.main()
