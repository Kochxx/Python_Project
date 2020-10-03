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
        self.assertEqual(main.tchacatchac(100), "100km/h -> 10:42")
        self.assertEqual(main.tchacatchac(200), "200km/h -> 09:51")
        self.assertEqual(main.tchacatchac(300), "300km/h -> 09:34")

    def testVitesse(self):
        """
           ..function: Tests the vitesse function
        """
        print("Test Vitesse()")
        self.assertEqual(main.vitesse()[0], "100km/h -> 10:42")
        self.assertEqual(main.vitesse()[10], "200km/h -> 09:51")
        self.assertEqual(main.vitesse()[15], "250km/h -> 09:40")


if __name__ == '__main__':
    unittest.main()
