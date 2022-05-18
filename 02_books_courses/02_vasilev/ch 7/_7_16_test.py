import math
from copy import deepcopy
from unittest import TestCase
import unittest

from _7_16 import Vector

class TestVector(TestCase):

    def setUp(self) -> None:
        self.a = Vector(1, 2, 3)
        self.b = Vector(2, 3, 4)

    def test_add(self):
        sum = self.a + self.b
        res = Vector(3, 5, 7)
        self.assertEqual(sum, res)
        self.assertEqual(self.a, Vector(1, 2, 3))
        self.assertEqual(self.b, Vector(2, 3, 4))

    def test_str(self):
        self.assertEqual(str(self.a), '<1|2|3>')

    def test_mul_num(self):
        mul = self.a * 5
        res = Vector(5, 10, 15)
        self.assertEqual(mul, res)

    def test_rmul_num(self):
        mul = 5 * self.a
        res = Vector(5, 10, 15)
        self.assertEqual(mul, res)

    def test_mul_vector(self):
        mul = self.a * self.b
        self.assertEqual(mul, 20.0)

    def test_neg(self):
        neg = Vector(-1, -2, -3)
        self.assertEqual(-self.a, neg)
        self.assertEqual(self.a, Vector(1, 2, 3))

    def test_sub(self):
        sub = self.a - self.b
        res = Vector(-1, -1, -1)

        self.assertEqual(sub, res)

    def test_rsub(self):
        pass

    def test_abs(self):
        abs_vector = abs(self.a)
        res = math.sqrt(1 * 1 + 2 * 2 + 3 * 3)
        self.assertEqual(abs_vector, res)

    def test_true_div(self):
        true_div = self.a / 2
        res = Vector(1 / 2, 2 / 2, 3 / 2)
        self.assertEqual(true_div, res)

    def test_ne(self):
        ne_res = (self.a != self.b)
        self.assertEqual(ne_res, True)

    def test_lt(self):
        lt_res_1 = abs(self.a) < abs(self.b)
        lt_res_2 = abs(self.b) > abs(self.a)
        self.assertEqual(lt_res_1, True)
        self.assertEqual(lt_res_2, True)

    def test_gt(self):
        gt_res_1 = abs(self.a) > abs(self.b)
        gt_res_2 = abs(self.b) > abs(self.a)
        self.assertEqual(gt_res_1, False)
        self.assertEqual(gt_res_2, True)

    def test_le(self):
        le_res_1 = abs(self.a) <= abs(self.b)
        va = Vector(1, 2, 3)
        vb = Vector(2, 1, 3)
        le_res_2 = abs(va) <= abs(vb)
        le_res_3 = abs(self.b) <= abs(self.a)

        self.assertEqual(le_res_1, True)
        self.assertEqual(le_res_2, True)
        self.assertEqual(le_res_3, False)

    def test_ge(self):
        ge_res_1 = abs(self.b) >= abs(self.a)
        va = Vector(1, 2, 3)
        vb = Vector(2, 1, 3)
        ge_res_2 = abs(va) >= abs(vb)
        ge_res_3 = abs(self.a) >= abs(self.b)

        self.assertEqual(ge_res_1, True)
        self.assertEqual(ge_res_2, True)
        self.assertEqual(ge_res_3, False)

    def test_lshift(self):
        lshift_1 = deepcopy(self.a << 1)
        res_1 = Vector(2, 3, 1)
        lshift_2 = deepcopy(self.a << 2)
        res_2 = Vector(1, 2, 3)

        self.assertEqual(lshift_1, res_1)
        self.assertEqual(lshift_2, res_2)

    def test_rlshift(self):
        lshift_1 = deepcopy(1 << self.a)
        res_1 = Vector(3, 1, 2)
        lshift_2 = deepcopy(2 << self.a)
        res_2 = Vector(1, 2, 3)

        self.assertEqual(lshift_1, res_1)
        self.assertEqual(lshift_2, res_2)

    def test_rshift(self):
        rshift_1 = deepcopy(self.a >> 1)
        res_1 = Vector(3, 1, 2)
        rshift_2 = deepcopy(self.a >> 2)
        res_2 = Vector(1, 2, 3)

        self.assertEqual(rshift_1, res_1)
        self.assertEqual(rshift_2, res_2)

    def test_rrshift(self):
        rlshift_1 = deepcopy(1 >> self.a)  # self.a << 1, sefl.a >> 1
        res_1 = Vector(2, 3, 1)
        rlshift_2 = deepcopy(2 >> self.a)
        res_2 = Vector(1, 2, 3)

        self.assertEqual(rlshift_1, res_1)
        self.assertEqual(rlshift_2, res_2)

if __name__ == '__main__':
    unittest.main()
        