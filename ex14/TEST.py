import main
import unittest


class Test(unittest.TestCase):

    def TestValue(self):
        self.assertEqual(main.objet.y, 28)
        self.assertEqual(main.objet.x, 23)
        self.assertEqual(main.objet.affiche(), "(28, 42)")


if __name__ == '__main__':
    unittest.main()
