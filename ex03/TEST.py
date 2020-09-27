import main
import unittest
import random


class Test(unittest.TestCase):
    # test the value error
    def testRaiseValueTypeError(self):
        print("testRaiseValueTypeError")
        self.assertRaises(ValueError, main.squareRoot, -8.5)
        print("Incorrect value => expected value none negative")

    # test value
    def testValue(self):
        print("testValue")
        self.assertEqual(main.squareRoot(9), 3)
        self.assertEqual(main.squareRoot(25), 5)


if __name__ == '__main__':
    unittest.main()
