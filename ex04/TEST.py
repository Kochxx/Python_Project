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
        test1 = main.ex04()
        self.assertEqual(test1.secure(2.5, 9), "KO")
        self.assertEqual(test1.secure(10, 800), "KO")
        self.assertEqual(test1.secure(2.31, 7.411), "KO")

    def testValueOK(self):
        """
        ..function:: test value to obtain "OK" result
        """
        print("Test Value OK")
        test2 = main.ex04()
        self.assertEqual(test2.secure(2.3, 7.41), "OK")
        self.assertEqual(test2.secure(1.5, 5.4), "OK")
        self.assertEqual(test2.secure(0.789, 6.985), "OK")

    def testValueAugmenter(self):
        """
        ..function:: test value to obtain "Augmenter" result
        """
        print("Test Value Augmenter")
        test3 = main.ex04()
        self.assertEqual(test3.secure(4.0, 7.41), "Augmenter")
        self.assertEqual(test3.secure(850.2, 6.1), "Augmenter")
        self.assertEqual(test3.secure(51.5, 6.985), "Augmenter")

    def testValueDiminuer(self):
        """
        ..function:: test value to obtain "Diminuer" result
        """
        print("Test Value Augmenter")
        test4 = main.ex04()
        self.assertEqual(test4.secure(2.3, 50.6), "Diminuer")
        self.assertEqual(test4.secure(1.5, 7890.4), "Diminuer")
        self.assertEqual(test4.secure(0.789, 9.9485), "Diminuer")


if __name__ == '__main__':
    unittest.main()
