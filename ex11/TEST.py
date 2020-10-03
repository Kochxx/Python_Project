import main
import unittest
import random


class Test(unittest.TestCase):
    # test the value error
    def testASmallerThanB(self):
        print("testASmallerThanB")
        self.assertRaises(ValueError,main.sortList,1,5)
        print("Incorrect value => expected value none negative")

    # test value
    def testExpectedResult(self):
        print("testExpectedResult")
        self.assertEqual(main.sortList("abc", "de"), ['ad', 'ae', 'bd', 'be', 'cd', 'ce'])
        print("testExpectedResult successful")

if __name__ == '__main__':
    unittest.main()