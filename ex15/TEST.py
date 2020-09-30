import main
import unittest
import random


class Test(unittest.TestCase):
    """
    ..class:: Test class

    """
    def testValueVecteurWithParameters(self):
        """
        ..function:: Test to checks the value of a vector init by parameters
        """
        print("Test Value Init Parameters")
        vecteur = main.Vecteur2D()
        main.Vecteur2D.__init__(vecteur, 1, 2)
        self.assertEqual(vecteur.x, 1)
        self.assertEqual(vecteur.y, 2)

    def testValueVecteurDefault(self):
        """
        ..function:: Test to checks the value of a vector init by default
        """
        print("Test Value Init Default")
        vecteur = main.Vecteur2D()
        main.Vecteur2D.__init__(vecteur)
        self.assertEqual(vecteur.x, 0)
        self.assertEqual(vecteur.y, 0)


if __name__ == '__main__':
    unittest.main()
