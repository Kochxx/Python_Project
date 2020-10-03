import main
import unittest
import random


class Test(unittest.TestCase):
    # test the value error
    def testASmallerThanB(self):
        print("testASmallerThanB")
        self.assertRaises(ValueError, main.compterMots, "")
        print("Incorrect value => expected value not empty string")

    # test value
    def testValue(self):
        print("testSuccessfulInput")
        self.assertEqual(main.compterMots("test du test ce de ce test testant testant"), {'ce': 2, 'de': 1, 'du': 1, 'test': 3, 'testant': 2})
        print("testSuccessfulInput succeded")


if __name__ == '__main__':
    unittest.main()
