#!/usr/bin/python3
"""unittest for square module and Square class"""


import unittest
import models.square as sqr
from models.square import Square
import io
import sys


class Test_Square(unittest.TestCase):
    """class contains test for Square class"""

    def test_module_doc(self):
        self.assertTrue(len(sqr.__doc__) > 1)

    def test_class_doc(self):
        self.assertTrue(len(Square.__doc__) > 1)

    def test_instantiation(self):
        a = Square(2, 5)


class Test_Args_Type(unittest.TestCase):
    """test class argument types"""

    def test_0_argc(self):
        with self.assertRaises(TypeError):
            a = Square()

    def test_non_keyworded_args(self):
        s1 = Square(10, 10, 10, 10)
        self.assertTrue(s1.id > 0)


class Test_attributes(unittest.TestCase):
    """test class attributes"""

    def test_size(self):
        s1 = Square(10, 10, 10, 10)
        s1.size = 20
        self.assertEqual(s1.width, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = -20

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = "str"

    def test_x(self):
        s1 = Square(10, 10, 10, 10)
        s1.x = 15
        self.assertEqual(s1.x, 15)
        with self.assertRaises(ValueError):
            s1.x = -15
        with self.assertRaises(TypeError):
            s1.x = [1, 2, 3]

    def test_y(self):
        s1 = Square(10, 10, 10, 10)
        s1.y = 2
        self.assertEqual(s1.y, 2)
        with self.assertRaises(ValueError):
            s1.y = -9

        with self.assertRaises(TypeError):
            s1.y = (1, 2)


class Test_area(unittest.TestCase):
    """test the area method of the class"""

    def test_with_small_numbers(self):
        s1 = Square(3, 3)
        self.assertEqual(s1.area(), 9)

    def test_with_large_numbers(self):
        s1 = Square(3500, 3500)
        self.assertEqual(s1.area(), 12250000)


class Test_display(unittest.TestCase):
    """test the display method"""

    @staticmethod
    def capture_output(sqr):
        capture = io.StringIO()
        sys.stdout = capture
        sqr.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_2d(self):
        s1 = Square(3)
        capture = Test_display.capture_output(s1)
        self.assertEqual(capture.getvalue(), "###\n###\n###\n")

    def test_2d_change_args(self):
        s1 = Square(3)
        s1.size = 4
        capture = Test_display.capture_output(s1)
        self.assertEqual(capture.getvalue(), "####\n####\n####\n####\n")

    def test_3d(self):
        s1 = Square(3, 2, 2, 2)
        capture = Test_display.capture_output(s1)
        self.assertEqual(capture.getvalue(), "\n\n  ###\n  ###\n  ###\n")


class Test__str__(unittest.TestCase):
    """test the __str__ method"""

    @staticmethod
    def capture_output(sqr):
        capture = io.StringIO()
        sys.stdout = capture
        print(sqr)
        sys.stdout = sys.__stdout__
        return capture

    def test_str(self):
        s1 = Square(4, 2, 1, 12)
        capture = Test__str__.capture_output(s1)
        self.assertEqual(capture.getvalue(), "[Square] (12) 2/1 - 4\n")

    def test_changed(self):
        s1 = Square(4, 2, 1, 12)
        s1.width = 2
        s1.height = 4
        s1.x = 1
        s1.y = 1
        s1.id = 89

        capture = Test__str__.capture_output(s1)
        self.assertEqual(capture.getvalue(), "[Square] (89) 1/1 - 2\n")


class Test_Update(unittest.TestCase):
    """test the update method"""

    @staticmethod
    def output(rect):
        capture = io.StringIO()
        sys.stdout = capture
        print(rect)
        sys.stdout = sys.__stdout__
        return capture

    def test_one_args(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89)
        cap = Test_Update.output(s1)
        self.assertEqual(cap.getvalue(), "[Square] (89) 10/10 - 10\n")

    def test_two_args(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 5)
        cap = Test_Update.output(s1)
        self.assertEqual(cap.getvalue(), "[Square] (89) 10/10 - 5\n")

    def test_3_args(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 5, 2)
        cap = Test_Update.output(s1)
        self.assertEqual(cap.getvalue(), "[Square] (89) 2/10 - 5\n")

    def test_4_args(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 5, 1, 10)
        cap = Test_Update.output(s1)
        self.assertEqual(cap.getvalue(), "[Square] (89) 1/10 - 5\n")

    def test_0_args(self):
        s1 = Square(10, 10, 10, 10)
        s1.update()
        cap = Test_Update.output(s1)
        self.assertEqual(cap.getvalue(), "[Square] (10) 10/10 - 10\n")

    def test_kwargs_id(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(id=89)
        cap = Test_Update.output(s1)
        self.assertEqual(cap.getvalue(), "[Square] (89) 10/10 - 10\n")

    def test_kwargs_size(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(size=5)
        cap = Test_Update.output(s1)
        self.assertEqual(cap.getvalue(), "[Square] (10) 10/10 - 5\n")

    def test_kwargs_x(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(x=1)
        cap = Test_Update.output(s1)
        self.assertEqual(cap.getvalue(), "[Square] (10) 1/10 - 10\n")

    def test_kwargs_y(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(y=4)
        cap = Test_Update.output(s1)
        self.assertEqual(cap.getvalue(), "[Square] (10) 10/4 - 10\n")

    def test_kwargs_all(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(y=4, size=5, x=2, height=5, id=89)
        cap = Test_Update.output(s1)
        self.assertEqual(cap.getvalue(), "[Square] (89) 2/4 - 5\n")


class Test_To_Dictionary(unittest.TestCase):
    """test the to_dictionary method"""

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        dic = {'id': s1.id, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1.to_dictionary(), dic)
