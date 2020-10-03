import main
import unittest


class Test(unittest.TestCase):
    """
    ..class:: Test class

    """
    def testValueY(self):
        """
        ..function:: Test value of the attribute Y
        """
        print("Test Value Y")
        self.assertEqual(main.MaClasse.y, 28)
        self.assertNotEqual(main.MaClasse.y, 23)

    def testValueX(self):
        """
        ..function:: Test value of the attribute X
        """
        print("Test Value X")
        self.assertEqual(main.MaClasse.x, 23)
        self.assertNotEqual(main.MaClasse.x, 28)

    def testAffiche(self):
        """
        ..function:: Test the function affiche()
        """
        print("Test affiche()")
        test = main.MaClasse()
        self.assertEqual(test.affiche(), "(28, 42)")


if __name__ == '__main__':
    unittest.main()
