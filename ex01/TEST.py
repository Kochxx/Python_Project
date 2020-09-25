import main
import unittest
import random


class Test(unittest.TestCase):
    #tests the value 0 for the denominator and then for the numerator.
    def testZeroDivision(self):
        print("Zero Division Test")
        self.assertEqual(main.handling(1, 0.0), 0.0)
        self.assertRaises(ZeroDivisionError, main.handling(0.0, 1.0))

    #tests the value obtained by the handling function
    def testValueVitesse(self):
        print("Value Vitesse Test")
        self.assertEqual(float('{:.1f}'.format(main.handling(7.8, 4.0))), 0.5)
        self.assertEqual(float('{:.1f}'.format(main.handling(9.0, 3))), 0.3)
        self.assertEqual(float('{:.1f}'.format(main.handling(2, 10.0))), 5)


if __name__ == '__main__':
    unittest.main()
