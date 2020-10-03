import main
import unittest
import random


class Test(unittest.TestCase):
    """
        ..class:: Test class ex02
    """

    def testRaiseValueTypeError(self):
        """
            ..function:: Test the value error
        """
        print("testRaiseValueTypeError")
        self.assertRaises(ValueError, main.squareRoot, -8.5)
        print("Incorrect value => expected value none negative")

    def testValue(self):
        """
            ..function:: Test the value
        """
        print("testValue")
        self.assertEqual(main.squareRoot(9), 3)
        self.assertEqual(main.squareRoot(25), 5)


if __name__ == '__main__':
    unittest.main()
