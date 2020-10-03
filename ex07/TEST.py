import main
import unittest
import random


class Test(unittest.TestCase):
    """
    ..class:: Test class

    """
    def testmaFonction(self):
        """
         ..function:: Tests the value returned by maFonction()
         """
        print("Test maFonction()")
        self.assertEqual(main.maFonction(1), -2)
        self.assertEqual(main.maFonction(3), 52)
        self.assertEqual(main.maFonction(161651861651641), 8448354465425976475251319473446222234124288)

    def testTabuler(self):
        """
         ..function:: Tests the value returned by maFonction()
         """
        print("Test tabuler()")
        self.assertEqual(main.tabuler('maFonction', 0, 10, 1), [-5, -2, 13, 52, 127, 250, 433, 688, 1027, 1462])
        self.assertEqual(main.tabuler('maFonction', 2, 40, 4), [13, 433, 2005, 5497, 11677, 21313, 35173, 54025, 78637, 109777])
        self.assertEqual(main.tabuler('maFonction', 10, 20, 1), [2005, 2668, 3463, 4402, 5497, 6760, 8203, 9838, 11677, 13732])
        self.assertRaises(ValueError, main.tabuler('maFonction', 40, 2, 4))
        self.assertRaises(ValueError, main.tabuler('maFonction', 2, 12, 0))


if __name__ == '__main__':
    unittest.main()
