import main
import unittest


class Test(unittest.TestCase):
    """
    ..class:: Test Class

    """

    def testInit(self):
        """
        ..function: tests the init of the class ex09

        """
        print("Test Init of the Class ex09")
        test1 = main.ex09()
        self.assertEqual(sorted(test1.liste), sorted([10, 17, 25, 38, 72]))

    def testGetList(self):
        """
        ..function: tests the function getList()

        """
        print("Test getList()")
        test2 = main.ex09()
        self.assertEqual(sorted(test2.getList()), sorted([10, 17, 25, 38, 72]))

    def testActionAdd(self):
        """
        ..function: tests the function action() for the add operation

        """
        print("Test Add of action()")
        test3 = main.ex09()
        self.assertEqual(test3.action('add', 3), [17, 38, 10, 25, 72, 3])
        self.assertEqual(test3.action('add', 1941717), [17, 38, 10, 25, 72, 3, 1941717])
        self.assertEqual(test3.action('add', -894), [17, 38, 10, 25, 72, 3, 1941717, -894])
        self.assertEqual(test3.action('add', 181888888888), [17, 38, 10, 25, 72, 3, 1941717, -894, 181888888888])

    def testActionRemove(self):
        """
        ..function: tests the function action() for the remove operation

        """
        print("Test Remove of action()")
        test4 = main.ex09()
        self.assertEqual(test4.action('remove', 17), [38, 10, 25, 72])
        self.assertEqual(test4.action('remove', 10), [38, 25, 72])
        self.assertEqual(test4.action('remove', 38), [25, 72])
        self.assertEqual(test4.action('remove', 72), [25])

    def testActionReverse(self):
        """
        ..function: tests the function action() for the remove operation

        """
        print("Test Reverse of action()")
        test5 = main.ex09()
        self.assertEqual(test5.action('reverse'), [72, 25, 10, 38, 17])
        self.assertEqual(test5.action('reverse'), [17, 38, 10, 25, 72])

    def testActionSort(self):
        """
        ..function: tests the function action() for the sort operation

        """
        print("Test Sort of action()")
        test6 = main.ex09()
        self.assertEqual(test6.action('sort'), [10, 17, 25, 38, 72])

    def testActionPrintE(self):
        """
        ..function: tests the function action() for the printE operation

        """
        print("Test printE of action()")
        test7 = main.ex09()
        self.assertEqual(test7.action('printE', -1), 72)
        self.assertEqual(test7.action('printE', -4), 38)
        self.assertEqual(test7.action('printE', -2), 25)
        self.assertEqual(test7.action('printE', 3), 25)
        self.assertEqual(test7.action('printE', 4), 72)

    def testActionPrintI(self):
        """
        ..function: tests the function action() for the printI operation

        """
        print("Test printI of action()")
        test8 = main.ex09()
        self.assertEqual(test8.action('printI', 17), 0)
        self.assertEqual(test8.action('printI', 72), 4)
        self.assertEqual(test8.action('printI', 38), 1)
        self.assertEqual(test8.action('printI', 25), 3)
        self.assertEqual(test8.action('printI', 10), 2)

    def testSubList(self):
        """
        ..function: tests the function subList()

        """
        print("Test subList()")
        test9 = main.ex09()
        self.assertEqual(test9.subList(1, 3), [38, 10])
        self.assertEqual(test9.subList('oui', 3), [17, 38, 10])
        self.assertEqual(test9.subList(2, 'oui'), [10, 25, 72])
        self.assertEqual(test9.subList('oui', 'oui'), [17, 38, 10, 25, 72])
        with self.assertRaises(Exception):
            test9.subList('non', 1)
        with self.assertRaises(Exception):
            test9.subList('cevscc', 'wsecw')


if __name__ == '__main__':
    unittest.main()
