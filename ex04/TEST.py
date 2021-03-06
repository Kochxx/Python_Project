import main
import unittest
import random


class Test(unittest.TestCase):
    """
    ..class:: Test class ex04

    """

    def testValueKO(self):
        """
        ..function:: test value to obtain "KO" result
        """
        print("Test Value KO")
        self.assertEqual(main.secure(2.5, 9), "KO")
        self.assertEqual(main.secure(10, 800), "KO")
        self.assertEqual(main.secure(2.31, 7.411), "KO")

    def testValueOK(self):
        """
        ..function:: test value to obtain "OK" result
        """
        print("Test Value OK")
        self.assertEqual(main.secure(2.3, 7.41), "OK")
        self.assertEqual(main.secure(1.5, 5.4), "OK")
        self.assertEqual(main.secure(0.789, 6.985), "OK")

    def testValueAugmenter(self):
        """
        ..function:: test value to obtain "Augmenter" result
        """
        print("Test Value Augmenter")
        self.assertEqual(main.secure(4.0, 7.41), "Augmenter")
        self.assertEqual(main.secure(850.2, 6.1), "Augmenter")
        self.assertEqual(main.secure(51.5, 6.985), "Augmenter")

    def testValueDiminuer(self):
        """
        ..function:: test value to obtain "Diminuer" result
        """
        print("Test Value Augmenter")
        self.assertEqual(main.secure(2.3, 50.6), "Diminuer")
        self.assertEqual(main.secure(1.5, 7890.4), "Diminuer")
        self.assertEqual(main.secure(0.789, 9.9485), "Diminuer")


if __name__ == '__main__':
    unittest.main()
