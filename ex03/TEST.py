import main
import unittest
import random


class Test(unittest.TestCase):
    # test the value error
    def testRaiseValueTypeError(self):
        print("testRaiseValueTypeError")
        self.assertRaises(ValueError, main.ex03, -8.5, 5)
        print("Incorrect value => expected value string")

    def testASmallerThanB(self):
        print("testASmallerThanB")
        self.assertEqual(main.ex03("albatros","belgique"), "albatros")
        print("testASmallerThanB successful")

    def testBSmallerThanA(self):
        print("testBSmallerThanA")
        self.assertEqual(main.ex03("belgique","albatros"), "albatros")
        print("testBSmallerThanA successful")

    def testBSmallerThanA(self):
        print("testBSmallerThanA")
        self.assertEqual(main.ex03("5","3"), "3")
        print("testBSmallerThanA successful")

    def testAEqualsB(self):
        print("testAEqualsB")
        self.assertEqual(main.ex03("albatros","albatros"), "albatros")
        print("testAEqualsB successful")



if __name__ == '__main__':
    unittest.main()
