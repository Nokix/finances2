import unittest
from List_Tools import flatten


class MyTestCase(unittest.TestCase):
    def test_flatten_1(self):
        self.assertListEqual(flatten([]), [])

    def test_flatten_2(self):
        self.assertListEqual(flatten([1, 2, 3]), [1, 2, 3])

    def test_flatten_3(self):
        self.assertListEqual(flatten([[1, 2], [[[3]]]]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
