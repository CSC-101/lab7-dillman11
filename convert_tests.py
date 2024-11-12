import unittest
import convert


class TestCases(unittest.TestCase):

    def test_str_to_float(self):
        input = "5.12"
        result = convert.str_to_float(input)
        expected = 5.12
        self.assertEqual(expected, result)

    def test_str_to_float_2(self):
        input = "5"
        result = convert.str_to_float(input)
        expected = 5.0
        self.assertEqual(expected, result)

    def test_str_to_float_3(self):
        input = "hello"
        result = convert.str_to_float(input)
        expected = None
        self.assertEqual(expected, result)