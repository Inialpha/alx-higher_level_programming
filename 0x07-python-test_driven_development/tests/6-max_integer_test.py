#!/usr/bin/python3

"""module contains test suits for function max_integer(list=[])"""

import unittest
mod = __import__('6-max_integer')
test_max  = __import__('6-max_integer').max_integer
class Test_Max(unittest.TestCase):
    """class contains methods for testing function"""

    def test_mod_doc(self):
        self.assertTrue(len(mod.__doc__) > 1)

    def test_func_doc(self):
        self.assertTrue(len(test_max.__doc__) > 1)

    def test_argc(self):
        self.assertIsNone(test_max())

    def test_empty_list(self):
        li = []
        self.assertIsNone(test_max(li))

    def test_positive_list(self):
        my_list = [1, 2, 3, 4, 0]
        result = test_max(my_list)
        self.assertEqual(result, 4)

    def test_max_at_end(self):
        my_list = [1, 2, 3, 4, 0, 9]
        result = test_max(my_list)
        self.assertEqual(result, 9)

    def test_max_at_beginig(self):
        my_list = [10, 2, 3, 4, 0, 9]
        result = test_max(my_list)
        self.assertEqual(result, 10)

    def test_max_at_middle(self):
        my_list = [10, 2, 11, 4, 0, 9]
        result = test_max(my_list)
        self.assertEqual(result, 11)

    def test_negetive_list(self):
        my_list = [-1, -2, -3, -4,]
        result = test_max(my_list)
        self.assertEqual(result, -1)
    
    def test_negetive_beiginig(self):
        my_list = [-10, 2, 3, 4, 0, 9]
        result = test_max(my_list)
        self.assertEqual(result, 9)

    def test_negetive_end(self):
        my_list = [10, 2, 3, 4, 0, -9]
        result = test_max(my_list)
        self.assertEqual(result, 10)

    def test_negetive_middle(self):
        my_list = [10, 2, -3, -4, 0, 9]
        result = test_max(my_list)
        self.assertEqual(result, 10)

if __name__ == "__main__":
    unittest.main()
