import main
import unittest
import random


class Test(unittest.TestCase):
    def testZeroDivision(self):
        print("Zero Division Test")
        self.assertEqual(main.handling(1, 0.0), 0.0)
        with self.assertRaises(ZeroDivisionError):
            main.handling(0.0, 1)

    def

if __name__ == '__main__':
    unittest.main()
