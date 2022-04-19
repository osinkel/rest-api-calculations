import sys
import unittest

sys.path.append('../../')
from src.logic.math_logic import figure_out_operation


class TestMathLogic(unittest.TestCase):

    def test_add_operator(self):
        self.assertEqual(figure_out_operation('add', '1', '3.4'), '4.4')

    def test_sub_operator(self):
        self.assertEqual(figure_out_operation('sub', '1', '3.4'), '-2.4')

    def test_mod_operator(self):
        self.assertEqual(figure_out_operation('mod', '2', '3.4'), '2.0')

    def test_mul_operator(self):
        self.assertEqual(figure_out_operation('mul', '2', '3.4'), '6.8')

    def test_truediv_operator(self):
        self.assertEqual(figure_out_operation('truediv', '5', '2'), '2.5')

    def test_floordiv_operator(self):
        self.assertEqual(figure_out_operation('floordiv', '5', '2'), '2.0')

    def test_pow_operator(self):
        self.assertEqual(figure_out_operation('pow', '5', '2'), '25.0')

    def test_rshift_operator(self):
        self.assertEqual(figure_out_operation('rshift', '5', '2'), '1')

    def test_lshift_operator(self):
        self.assertEqual(figure_out_operation('lshift', '5', '2'), '20')

    def test_gt_operator(self):
        self.assertEqual(figure_out_operation('gt', '5', '2'), 'True')

    def test_divide_by_zero(self):
        self.assertEqual(figure_out_operation('floordiv', '1', '0'), '')
        self.assertEqual(figure_out_operation('truediv', '1', '0'), '')

    def test_bad_operator(self):
        self.assertEqual(figure_out_operation('oper', '1', '3.4'), '')

    def test_bad_numbers(self):
        self.assertEqual(figure_out_operation('add', 'val', '3.4'), '')
        self.assertEqual(figure_out_operation('add', '1', 'val'), '')
        self.assertEqual(figure_out_operation('add', '1', ''), '')
        self.assertEqual(figure_out_operation('add', '', '3.4'), '')
        