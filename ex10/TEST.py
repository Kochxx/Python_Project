import main
import unittest


class Test(unittest.TestCase):

    # test function comprehensionList()
    def testListValue(self):
        self.assertEqual(main.comprehensionList(), [5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()
