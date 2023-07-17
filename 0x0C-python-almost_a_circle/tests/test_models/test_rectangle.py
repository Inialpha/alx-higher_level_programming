#!/usr/bin/python3
"""unittes for rectangle module and Rectangle class"""

import io
import sys
import unittest
import models.rectangle as rect
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """class contains test for Rectangle class"""

    def test_module_doc(self):
        self.assertTrue(len(rect.__doc__) > 1)

    def test_class_doc(self):
        self.assertTrue(len(Rectangle.__doc__) > 1)

    def test_instantiation(self):
        a = Rectangle(2, 5)


class Test_Args_Type(unittest.TestCase):
    """test class arguments type"""

    def test_0_argc(self):
        with self.assertRaises(TypeError):
            a = Rectangle()

    def test_1_argc(self):
        with self.assertRaises(TypeError):
            a = Rectangle(2)

    def test_non_keyworded_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertTrue(r1.id > 0)


class Test_attributes(unittest.TestCase):
    """test class attributes"""

    def test_width(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.width = 20
        self.assertEqual(r1.width, 20)
        with self.assertRaises(ValueError):
            r1.width = -20

        with self.assertRaises(TypeError):
            r1.width = "str"

    def test_height(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.height = 50
        self.assertEqual(r1.height, 50)
        with self.assertRaises(ValueError):
            r1.height = -6

        with self.assertRaises(TypeError):
            r1.height = {'height': 5}

    def test_x(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.x = 15
        self.assertEqual(r1.x, 15)
        with self.assertRaises(ValueError):
            r1.x = -15
        with self.assertRaises(TypeError):
            r1.x = [1, 2, 3]

    def test_y(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.y = 2
        self.assertEqual(r1.y, 2)
        with self.assertRaises(ValueError):
            r1.y = -9

        with self.assertRaises(TypeError):
            r1.y = (1, 2)


class Test_area(unittest.TestCase):
    """test the area method"""

    def test_with_small_numbers(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_with_large_numbers(self):
        r1 = Rectangle(3500, 75000)
        self.assertEqual(r1.area(), 262500000)


class Test_display(unittest.TestCase):
    """test the display method"""

    @staticmethod
    def capture_output(rect):
        capture = io.StringIO()
        sys.stdout = capture
        rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_2d(self):
        r1 = Rectangle(3, 2)
        capture = Test_display.capture_output(r1)
        self.assertEqual(capture.getvalue(), "###\n###\n")

    def test_2d_change_args(self):
        r1 = Rectangle(3, 2)
        r1.width = 4
        r1.height = 3
        capture = Test_display.capture_output(r1)
        self.assertEqual(capture.getvalue(), "####\n####\n####\n")

    def test_3d(self):
        r1 = Rectangle(3, 2, 2, 2)
        capture = Test_display.capture_output(r1)
        self.assertEqual(capture.getvalue(), "\n\n  ###\n  ###\n")


class Test__str__(unittest.TestCase):
    """test the __str__ method"""

    @staticmethod
    def capture_output(rect):
        capture = io.StringIO()
        sys.stdout = capture
        print(rect)
        sys.stdout = sys.__stdout__
        return capture

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        capture = Test__str__.capture_output(r1)
        self.assertEqual(capture.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

    def test_changed(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1.width = 2
        r1.height = 4
        r1.x = 1
        r1.y = 1
        r1.id = 89

        capture = Test__str__.capture_output(r1)
        self.assertEqual(capture.getvalue(), "[Rectangle] (89) 1/1 - 2/4\n")


class Test_Update(unittest.TestCase):
    """test for the update method"""

    @staticmethod
    def output(rect):
        capture = io.StringIO()
        sys.stdout = capture
        print(rect)
        sys.stdout = sys.__stdout__
        return capture

    def test_one_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        cap = Test_Update.output(r1)
        self.assertEqual(cap.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

    def test_two_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 5)
        cap = Test_Update.output(r1)
        self.assertEqual(cap.getvalue(), "[Rectangle] (89) 10/10 - 5/10\n")

    def test_3_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 5, 2)
        cap = Test_Update.output(r1)
        self.assertEqual(cap.getvalue(), "[Rectangle] (89) 10/10 - 5/2\n")

    def test_4_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 5, 2, 1)
        cap = Test_Update.output(r1)
        self.assertEqual(cap.getvalue(), "[Rectangle] (89) 1/10 - 5/2\n")

    def test_5_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 5, 2, 1, 3)
        cap = Test_Update.output(r1)
        self.assertEqual(cap.getvalue(), "[Rectangle] (89) 1/3 - 5/2\n")

    def test_0_args(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update()
        cap = Test_Update.output(r1)
        self.assertEqual(cap.getvalue(), "[Rectangle] (10) 10/10 - 10/10\n")

    def test_kwargs_id(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(id=89)
        cap = Test_Update.output(r1)
        self.assertEqual(cap.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

    def test_kwargs_width(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(width=5)
        cap = Test_Update.output(r1)
        self.assertEqual(cap.getvalue(), "[Rectangle] (10) 10/10 - 5/10\n")

    def test_kwargs_height(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(height=3)
        cap = Test_Update.output(r1)
        self.assertEqual(cap.getvalue(), "[Rectangle] (10) 10/10 - 10/3\n")

    def test_kwargs_x(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(x=1)
        cap = Test_Update.output(r1)
        self.assertEqual(cap.getvalue(), "[Rectangle] (10) 1/10 - 10/10\n")

    def test_kwargs_y(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(y=4)
        cap = Test_Update.output(r1)
        self.assertEqual(cap.getvalue(), "[Rectangle] (10) 10/4 - 10/10\n")

    def test_kwargs_all(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(y=4, width=5, x=2, height=3, id=89)
        cap = Test_Update.output(r1)
        self.assertEqual(cap.getvalue(), "[Rectangle] (89) 2/4 - 5/3\n")


class Test_to_dictionary(unittest.TestCase):
    """test to_dictionary method"""

    def test_Rectangle_to_dict(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        new = {'x': 1, 'y': 9, 'id': r1.id, 'height': 2, 'width': 10}
        self.assertEqual(r1.to_dictionary(), new)
