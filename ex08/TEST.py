import main
import unittest


class Test(unittest.TestCase):
    """
       ..class:: Test class

    """

    def testTchacatchac(self):
        """
           ..function: Tests the tchacatchac function
        """
        print("Test Tchacatchac()")
        test1 = main.ex08()
        self.assertEqual(test1.tchacatchac(100), "100km/h -> 10:42")
        self.assertEqual(test1.tchacatchac(200), "200km/h -> 9:51")
        self.assertEqual(test1.tchacatchac(300), "300km/h -> 9:34")

    def testVitesse(self):
        """
           ..function: Tests the vitesse function
        """
        print("Test Vitesse()")
        test2 = main.ex08()
        self.assertEqual(test2.vitesse()[0], "100km/h -> 10:42")
        self.assertEqual(test2.vitesse()[10], "200km/h -> 9:51")
        self.assertEqual(test2.vitesse()[15], "250km/h -> 9:40")


if __name__ == '__main__':
    unittest.main()
