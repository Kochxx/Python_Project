import main
import unittest
import random


class Test(unittest.TestCase):
    """
    ..class:: Test Class

    """
    def testCube(self):
        """
        ..function: Test cube function
        """
        print("test cube()")
        test1 = main.ex06()
        self.assertEqual(test1.cube(1), 1)
        self.assertEqual(test1.cube(30), 27000.0)
        self.assertEqual(test1.cube(5), 125)

    def testVolumeSphere(self):
        """
        ..function: Test volume sphere function
        """
        print("test vSphere()")
        test2 = main.ex06()
        self.assertEqual(float('{:.1f}'.format(test2.vSphere(5))), 1570.8)
        self.assertEqual(float('{:.1f}'.format(test2.vSphere(651))), 3466991921.7)
        self.assertEqual(float('{:.1f}'.format(test2.vSphere(2))), 100.5)
        self.assertEqual(float('{:.1f}'.format(test2.vSphere(1))), 12.6)


if __name__ == '__main__':
    unittest.main()
