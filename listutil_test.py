import unittest
from listutil import unique


class ListUtilTest(unittest.TestCase):

    def test_single_item_list(self):
        self.assertListEqual(['hi'], unique(['hi']))

    def test_borderline_cases(self):
        self.assertListEqual([0, 1], unique([0, 0, 1, 1]))

    def test_typical_cases(self):
        self.assertListEqual(["a", "c"], unique(["a", "c"]))

    def test_empty_list(self):
        self.assertListEqual([], unique([]))

    def test_one_item_many_times(self):
        self.assertListEqual(["k"], unique(["k", "k", "k", "k", "k", "k", "k", "k", "k"]))

    def test_many_items_list(self):
        self.assertListEqual([1, 2, "k"], unique([1, 1, 1, 1, 2, 2, "k", "k", "k"]))


if __name__ == '__main__':
    unittest.main()