import main
import unittest
import random


class Test(unittest.TestCase):
    # test the value error
    def testRaiseValueTypeError(self):
        print("testRaiseValueTypeError")
        self.assertRaises(AttributeError, main.smallest, -8.5, 5)
        print("Incorrect value => expected value string")

    def testASmallerThanB(self):
        print("testASmallerThanB")
        self.assertEqual(main.smallest("albatros", "belgique"), "albatros")
        print("testASmallerThanB successful")

    def testBSmallerThanA(self):
        print("testBSmallerThanA")
        self.assertEqual(main.smallest("belgique", "albatros"), "albatros")
        print("testBSmallerThanA successful")

    def testBSmallerThanA2(self):
        print("testBSmallerThanA")
        self.assertEqual(main.smallest("5", "3"), "3")
        print("testBSmallerThanA successful")

    def testAEqualsB(self):
        print("testAEqualsB")
        self.assertEqual(main.smallest("albatros", "albatros"), "albatros")
        print("testAEqualsB successful")



if __name__ == '__main__':
    unittest.main()
