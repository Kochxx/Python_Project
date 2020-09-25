import main
import unittest


class Test(unittest.TestCase):

    # test value of the attribute Y
    def testValueY(self):
        print("Test Value Y")
        self.assertEqual(main.MaClasse.y, 28)
        self.assertNotEqual(main.MaClasse.y, 23)

    # test value of the attribute X
    def testValueX(self):
        print("Test Value X")
        self.assertEqual(main.MaClasse.x, 23)
        self.assertNotEqual(main.MaClasse.x, 28)


if __name__ == '__main__':
    unittest.main()
