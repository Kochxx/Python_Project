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
        self.assertEqual(str(sorted(main.getX())), "['a', 'b', 'c', 'd']")

    def testSetY(self):
        """
        ..function:: Test the function getY()
        """
        print("Test getY()")
        self.assertEqual(str(sorted(main.getY())), "['b', 'd', 's']")

    def testInitialSets(self):
        """
        ..function:: Test the function setsInitial()
        """
        print("Test Displays of the sets X and Y")
        self.assertEqual(main.setsInitial({'a', 'b', 'c', 'd'}, {'s', 'b', 'd'})[0], "X : {'a', 'b', 'c', 'd'}")
        self.assertEqual(main.setsInitial({'a', 'b', 'c', 'd'}, sorted({'s', 'b', 'd'}))[1], "Y : {'b', 'd', 's'}")

    def testAppartenanceOperation(self):
        """
        ..function:: Test of function appartenance()
        """
        print("Test the 'appartenance' operation between an element and a set ")
        self.assertEqual(main.appartenance('a', 'X')[0], "a in X : True")
        self.assertEqual(main.appartenance('z', 'Y')[0], "z in Y : False")

    def testOperation(self):
        """
        ..function:: Test of function operations()
        """
        print("Test the different function between two sets")
        self.assertEqual(main.operation('X', 'Y', 'union'), "X union Y : {'a', 'b', 'c', 'd', 's'}")
        self.assertEqual(main.operation('Y', 'X', 'union'), "Y union X : {'a', 'b', 'c', 'd', 's'}")
        self.assertEqual(main.operation('X', 'Y', 'inter'), "X inter Y : {'b', 'd'}")
        self.assertEqual(main.operation('Y', 'X', 'inter'), "Y inter X : {'b', 'd'}")
        self.assertEqual(main.operation('X', 'Y', '-'), "X - Y : {'a', 'c'}")
        self.assertEqual(main.operation('Y', 'X', '-'), "Y - X : {'s'}")


if __name__ == '__main__':
    unittest.main()
