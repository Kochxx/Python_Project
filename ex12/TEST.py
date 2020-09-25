import main
import unittest


class Test(unittest.TestCase):

    # test the function getX()
    def testSetX(self):
        print("Test getX()")
        self.assertEqual(str(main.getX()), "set(['a', 'c', 'b', 'd'])")

    # test the function getY()
    def testSetY(self):
        print("Test getY()")
        self.assertEqual(str(main.getY()), "set(['s', 'b', 'd'])")

    # test the function setsInitial()
    def testInitialSets(self):
        print("Test Displays of the sets X and Y")
        self.assertEqual(main.setsInitial({'a', 'b', 'c', 'd'}, {'s', 'b', 'd'})[0], "X : {'a','b', 'c', 'd'}")
        self.assertEqual(main.setsInitial({'a', 'b', 'c', 'd'}, {'s', 'b', 'd'})[1], "Y : {'s','b', 'd'}")

    # test of function appartenance()
    def testAppartenanceOperation(self):
        print("Test the 'appartenance' operation between an element and a set ")
        self.assertEqual(main.appartenance('a', 'X')[0], "a in X : True")
        self.assertEqual(main.appartenance('z', 'Y')[0], "z in Y : False")

    # test of function operations()
    def testOperation(self):
        print("Test the different function between two sets")
        self.assertEqual(main.operation('X', 'Y', 'union'), "X union Y : {'a', 'c', 'b', 'd', 's'}")
        self.assertEqual(main.operation('Y', 'X', 'union'), "Y union X : {'a', 's', 'b', 'd', 'c'}")
        self.assertEqual(main.operation('X', 'Y', 'inter'), "X inter Y : {'b', 'd'}")
        self.assertEqual(main.operation('Y', 'X', 'inter'), "Y inter X : {'b', 'd'}")
        self.assertEqual(main.operation('X', 'Y', '-'), "X - Y : {'a', 'c'}")
        self.assertEqual(main.operation('Y', 'X', '-'), "Y - X : {'s'}")


if __name__ == '__main__':
    unittest.main()
