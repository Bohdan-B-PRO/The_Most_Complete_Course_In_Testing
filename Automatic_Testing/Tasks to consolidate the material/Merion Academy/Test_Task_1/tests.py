import unittest
from main import*


class TestFunctions(unittest.TestCase):

    def test_make_cube(self):
        self.assertEqual(make_cube(3), 27)
        self.assertEqual(make_cube(0), 0)
        self.assertEqual(make_cube(-2), -8)

    def test_repeat(self):
        self.assertEqual(repeat("abc"), "abcabcabc")
        self.assertEqual(repeat(4), 8)
        self.assertNotEqual(repeat("a"), "aa")

    def test_create_powers(self):
        self.assertEqual(create_powers(2, 3, 4, p=2), [4, 9, 16])
        self.assertEqual(create_powers(1, p=3), [1])
        self.assertEqual(create_powers(2, 3, p=3), [8, 27])

    def test_reverse_number(self):
        self.assertEqual(reverse_number(123), 321)
        self.assertEqual(reverse_number(100), 1)
        self.assertEqual(reverse_number(0), 0)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

if __name__ == '__main__':
    unittest.main()