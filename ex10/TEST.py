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
        self.assertEqual(main.comprehensionList(), [5, 6, 7, 8])
        self.assertEqual(main.comprehensionList()[0], 5)


if __name__ == '__main__':
    unittest.main()
