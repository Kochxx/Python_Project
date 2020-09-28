import main
import unittest
import random


class Test(unittest.TestCase):
    # test the value error
    def testRaiseValueTypeError(self):
        print("testRaiseValueTypeError")
        self.assertRaises(ValueError, main.squareRoot, -8.5, 5)
        print("Incorrect value => expected value string")

    def testASmallerThanB(self):
        print("testASmallerThanB")
        self.assertEquals(main.smallestWord("albatros","belgique"), "albatros")
        print("testASmallerThanB successful")

    def testBSmallerThanA(self):
        print("testBSmallerThanA")
        self.assertEquals(main.smallestWord("belgique","albatros"), "albatros")
        print("testBSmallerThanA successful")

    def testAEqualsB(self):
        print("testAEqualsB")
        self.assertEquals(main.smallestWord("albatros","albatros"), "albatros")
        print("testAEqualsB successful")



if __name__ == '__main__':
    unittest.main()
