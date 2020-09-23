import main
import unittest
import random


class Test(unittest.TestCase):

    def testRaiseValueTypeError(self):
        print("Incorrect value => expected value none negative")
        self.assertRaises(ValueError, main.cube, -8.5)


if __name__ == '__main__':
    unittest.main()
