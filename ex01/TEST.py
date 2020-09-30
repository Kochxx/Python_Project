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
        test1 = main.ex1()
        self.assertEqual(test1.handling(1, 0.0), 0.0)
        self.assertRaises(ZeroDivisionError, test1.handling(0.0, 1.0))

    def testValueVitesse(self):
        """
        ..function:: tests the value obtained by the handling function
        """
        print("Value Vitesse Test")
        test2 = main.ex1()
        self.assertEqual(float('{:.1f}'.format(test2.handling(7.8, 4.0))), 0.5)
        self.assertEqual(float('{:.1f}'.format(test2.handling(9.0, 3))), 0.3)
        self.assertEqual(float('{:.1f}'.format(test2.handling(2, 10.0))), 5)


if __name__ == '__main__':
    unittest.main()
