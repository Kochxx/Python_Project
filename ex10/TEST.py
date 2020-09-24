import main
import unittest


class Test(unittest.TestCase):

    def tchacatchacTest(self):
        self.assertEqual(main.tchacatchac(100), "100km/h -> 10:42")


if __name__ == '__main__':
    unittest.main()
