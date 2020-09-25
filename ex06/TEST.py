import main
import unittest
import random


class Test(unittest.TestCase):

    # test cube function
    def testCube(self):
        print("test cube()")
        self.assertEqual(main.cube(1), 1)
        self.assertEqual(main.cube(30), 27000.0)
        self.assertEqual(main.cube(5), 125)

    # test volume sphere function
    def testVolumeSphere(self):
        print("test vSphere()")
        self.assertEqual(float('{:.1f}'.format(main.vSphere(5))), 1570.8)
        self.assertEqual(float('{:.1f}'.format(main.vSphere(651))), 3466991921.7)
        self.assertEqual(float('{:.1f}'.format(main.vSphere(2))), 100.5)
        self.assertEqual(float('{:.1f}'.format(main.vSphere(1))), 12.6)


if __name__ == '__main__':
    unittest.main()
