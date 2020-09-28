import main
import unittest


class Test(unittest.TestCase):
    """
    ..class:: Test class

    """
    # test the function getX()
    def testSetX(self):
        """
        ..function:: Test the function getX()
        """
        print("Test getX()")
        test1 = main.ex12()
        self.assertEqual(str(test1.getX()), "set(['a', 'c', 'b', 'd'])")

    def testSetY(self):
        """
        ..function:: Test the function getY()
        """
        print("Test getY()")
        test2 = main.ex12()
        self.assertEqual(str(test2.getY()), "set(['s', 'b', 'd'])")

    def testInitialSets(self):
        """
        ..function:: Test the function setsInitial()
        """
        print("Test Displays of the sets X and Y")
        test3 = main.ex12()
        self.assertEqual(test3.setsInitial({'a', 'b', 'c', 'd'}, {'s', 'b', 'd'})[0], "X : {'a','b', 'c', 'd'}")
        self.assertEqual(test3.setsInitial({'a', 'b', 'c', 'd'}, {'s', 'b', 'd'})[1], "Y : {'s','b', 'd'}")

    def testAppartenanceOperation(self):
        """
        ..function:: Test of function appartenance()
        """
        print("Test the 'appartenance' operation between an element and a set ")
        test4 = main.ex12()
        self.assertEqual(test4.appartenance('a', 'X')[0], "a in X : True")
        self.assertEqual(test4.appartenance('z', 'Y')[0], "z in Y : False")

    def testOperation(self):
        """
        ..function:: Test of function operations()
        """
        print("Test the different function between two sets")
        test5 = main.ex12()
        self.assertEqual(test5.operation('X', 'Y', 'union'), "X union Y : {'a', 'c', 'b', 'd', 's'}")
        self.assertEqual(test5.operation('Y', 'X', 'union'), "Y union X : {'a', 's', 'b', 'd', 'c'}")
        self.assertEqual(test5.operation('X', 'Y', 'inter'), "X inter Y : {'b', 'd'}")
        self.assertEqual(test5.operation('Y', 'X', 'inter'), "Y inter X : {'b', 'd'}")
        self.assertEqual(test5.operation('X', 'Y', '-'), "X - Y : {'a', 'c'}")
        self.assertEqual(test5.operation('Y', 'X', '-'), "Y - X : {'s'}")


if __name__ == '__main__':
    unittest.main()
