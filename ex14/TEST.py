import main
import unittest


class Test(unittest.TestCase):

    def TestValue(self):
      self.assertEqual(main.getY(), "set['s', 'b', 'd']")


if __name__ == '__main__':
    unittest.main()
