import main
import unittest
import random


class Test(unittest.TestCase):
    """
    ..class:: Test class

    """
    def testZeroDivision(self):
        """
        ..function:: Tests the value 0 for the denominator and then for the numerator.
        """
        print("Zero Division Test")
        self.assertEqual(main.speed(1, 0.0), 0.0)
        self.assertRaises(ZeroDivisionError, main.speed(0.0, 1.0))

    def testValueVitesse(self):
        """
        ..function:: tests the value obtained by the handling function
        """
        print("Value Vitesse Test")
        test2 = main.ex1()
        self.assertEqual(float('{:.8f}'.format(main.speed(7.8, 4.0))), 0.5)
        self.assertEqual(float('{:.8f}'.format(main.speed(9.0, 3))), 0.3)
        self.assertEqual(float('{:.8f}'.format(main.speed(2, 10.0))), 5)


if __name__ == '__main__':
    unittest.main()
