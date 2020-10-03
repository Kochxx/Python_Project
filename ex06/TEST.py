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
        self.assertEqual(main.cube(1), 1)
        self.assertEqual(main.cube(30), 27000.0)
        self.assertEqual(main.cube(5), 125)

    def testVolumeSphere(self):
        """
        ..function: Test volume sphere function
        """
        print("test vSphere()")
        self.assertEqual(float('{:.8f}'.format(main.vSphere(5))), 1570.79632679)
        self.assertEqual(float('{:.8f}'.format(main.vSphere(651))), 3466991921.7111564)
        self.assertEqual(float('{:.8f}'.format(main.vSphere(2))), 100.53096491)
        self.assertEqual(float('{:.8f}'.format(main.vSphere(1))), 12.56637061)


if __name__ == '__main__':
    unittest.main()
