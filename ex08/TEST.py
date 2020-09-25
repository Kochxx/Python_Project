import main
import unittest


class Test(unittest.TestCase):

    # test the tchacatchac function
    def testTchacatchac(self):
        print("Test Tchacatchac()")
        self.assertEqual(main.tchacatchac(100), "100km/h -> 10:42")
        self.assertEqual(main.tchacatchac(200), "200km/h -> 9:51")
        self.assertEqual(main.tchacatchac(300), "300km/h -> 9:34")

    # test the vitesse function
    def testVitesse(self):
        print("Test Vitesse()")
        self.assertEqual(main.vitesse()[0], "100km/h -> 10:42")
        self.assertEqual(main.vitesse()[10], "200km/h -> 9:51")
        self.assertEqual(main.vitesse()[15], "250km/h -> 9:40")


if __name__ == '__main__':
    unittest.main()
