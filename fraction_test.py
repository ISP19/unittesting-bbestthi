import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        f = Fraction(99)
        self.assertEqual("99", f.__str__())


    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        self.assertEqual(Fraction(16, 15), Fraction(2, 5) + Fraction(4, 6))
        self.assertEqual(Fraction(13, 14), Fraction(2, 4) + Fraction(3, 7))
        self.assertEqual(Fraction(17, 5), Fraction(2, 5) + Fraction(3, 1))
        self.assertEqual(Fraction(39, 5), Fraction(4, 5) + Fraction(7, 1))
        self.assertEqual(Fraction(13, 15), Fraction(1, 5) + Fraction(2, 3))
        self.assertEqual(Fraction(5, 6), Fraction(2, 4) + Fraction(2, 6))

    def test_mul(self):
        # 3/8 = 1/2 * 3/4
        self.assertEqual(Fraction(3, 5), Fraction(3, 5)*Fraction(1, 1))
        self.assertEqual(Fraction(1, 2), Fraction(3, 2)*Fraction(1, 3))
        self.assertEqual(Fraction(1, 1), Fraction(1, 2)*Fraction(2, 1))
        self.assertEqual(Fraction(1, 6), Fraction(1, 3)*Fraction(1, 2))
        self.assertEqual(Fraction(3, 5), Fraction(3, 5)*Fraction(1, 1))
        self.assertEqual(Fraction(4, 1), Fraction(6, 1)*Fraction(2, 3))
        self.assertEqual(Fraction(2, 1), Fraction(2, 7)*Fraction(7, 1))

    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        # TODO write more tests using other cases.
        # Consider special values like 0, 1/0, -1/0
        x = Fraction(1, 3)
        y = Fraction(-100, -300)
        z = Fraction(2, 5)
        self.assertTrue(x == y)
        self.assertTrue(x.__eq__(y))
        self.assertFalse(x == z)
        self.assertFalse(x.__eq__(z))

    def test_sub(self):
        # 1/35 = 3/7 - 2/5
        self.assertEqual(Fraction(3, 20), Fraction(2, 5)-Fraction(1, 4))
        self.assertEqual(Fraction(1, 4), Fraction(1, 2)-Fraction(1, 4))
        self.assertEqual(Fraction(19, 40), Fraction(3, 5)-Fraction(1, 8))
        self.assertEqual(Fraction(9, 26), Fraction(6, 13)-Fraction(3, 26))
        self.assertEqual(Fraction(27, 28), Fraction(5, 4)-Fraction(2, 7))
        self.assertEqual(Fraction(4, 5), Fraction(9, 5)-Fraction(3, 7))
        self.assertEqual(Fraction(7, 6), Fraction(2, 3)-Fraction(-3, 6))

    def test_div(self):
        # 7/8 = (1/4)/(2/7)
        self.assertEqual(Fraction(8, 15), Fraction(2, 5)/Fraction(3, 4))
        self.assertEqual(Fraction(21, 5), Fraction(3, 5)/Fraction(1, 7))
        self.assertEqual(Fraction(27, 14), Fraction(9, 7)/Fraction(2, 3))
        self.assertEqual(Fraction(8, 1), Fraction(2, 1)/Fraction(1, 4))
        self.assertEqual(Fraction(9, 10), Fraction(3, 4)/Fraction(5, 6))
        self.assertEqual(Fraction(8, 11), Fraction(2, 3)/Fraction(11, 12))
        self.assertEqual(Fraction(26, 99), Fraction(2, 9)/Fraction(11, 13))