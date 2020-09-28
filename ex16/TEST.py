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

    def testAddVectors(self):
        """
        ..function:: Test to checks the value of a vector with add function
        """
        print("Test Add Vectors")
        vecteur1 = main.Vecteur2D(2.1, 3.0)
        vecteur2 = main.Vecteur2D(12.3, 54.1, 2)
        vecteur1.__add__(vecteur2)
        self.assertEqual(vecteur1.x, 14.4)
        self.assertEqual(vecteur1.y, 57.1)


if __name__ == '__main__':
    unittest.main()
