import main
import unittest


class Test(unittest.TestCase):
    """
    ..class:: Test class
    """

    def testListValue(self):
        """
        ..function:: Test function comprehensionList()
        """
        print("Test Comprehension List")
        test1 = main.exo10()
        self.assertEqual(test1.comprehensionList(), [5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()
