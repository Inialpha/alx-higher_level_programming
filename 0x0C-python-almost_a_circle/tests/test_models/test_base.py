#!usr/bin/python3
"""unittest for base module"""

import os
import unittest
import models.base as base
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class Test_Base_instantiation(unittest.TestCase):
    """class contains methods for testing Base class"""

    def test_doctring(self):
        """test module docstring"""
        self.assertTrue(len(base.__doc__) > 1)

    def test_class_doc(self):
        """test class doctring"""
        self.assertTrue(len(Base.__doc__) > 1)

    def test_one_instance(self):
        a = Base()
        self.assertEqual(a.id, 1)

    def test_two_instances(self):
        a = Base()
        b = Base()
        self.assertEqual(a.id, b.id - 1)

    def test_instanciation_with_int(self):
        c = Base(89)
        self.assertTrue(c.id, 89)


class Test_To_Json_String(unittest.TestCase):

    def test_to_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(54, len(json_dictionary))

    def test_to_json_rectangle_type(self):
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(type(Base.to_json_string([r1.to_dictionary()])), str)

    def test_to_json_rectangle_two_list(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        dict_list = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(106, len(Base.to_json_string(dict_list)))

    def test_to_json_square_type(self):
        s1 = Square(10, 7, 2, 8)
        self.assertEqual(str, type(Base.to_json_string([s1.to_dictionary()])))

    def test_to_json_square_1_list(self):
        s1 = Square(10, 7, 2, 8)
        self.assertEqual(39, len(Base.to_json_string([s1.to_dictionary()])))

    def test_to_json_square_2_list(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(4, 5, 21, 2)
        slist = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertEqual(78, len(Base.to_json_string(slist)))

    def test_to_json_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_None(self):
        self.assertEqual("[]", Base.to_json_string(None))


class Test_Save_To_File(unittest.TestCase):
    """Test case for save_to_file method of Base class"""

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_1_Square(self):
        s1 = Square(10, 7, 2, 8)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            self.assertEqual(39, len(f.read()))

    def test_save_file_2_Square(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(20, 7, 2, 8)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertEqual(78, len(f.read()))

    def test_save_file_1_Rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(53, len(f.read()))

    def test_save_file_2_Rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(20, 14, 4, 16, 9)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(108, len(f.read()))

    def test_save_file_Base(self):
        b1 = Square(10, 7, 2, 8)
        Base.save_to_file([b1])
        with open("Base.json", "r") as f:
            self.assertEqual(39, len(f.read()))

    def test_save_to_file_None(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_2_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([1, 2], [])


class Test_From_Json_String(unittest.TestCase):
    """test cases for from_json_string method of the Base class"""

    def test_from_json_1_Square(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list)
        self.assertEqual(list_input, list_output)

    def test_from_json_2_Square(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list)
        self.assertEqual(list_input, list_output)

    def test_from_json_1_Rectangle(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list)
        self.assertEqual(list_input, list_output)

    def test_from_json_2_Rectangle(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list)
        self.assertEqual(list_input, list_output)

    def test_from_json_empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_2_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string("[{'id': 1}]", "str")


class Test_Create(unittest.TestCase):
    """Test cases for create method of Base class"""

    def test_creat_Rectangle_original(self):

        r1 = Rectangle(3, 5, 1, 2, 89)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (89) 1/2 - 3/5", str(r1))

    def test_creat_new_Rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 89)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (89) 1/2 - 3/5", str(r2))

    def test_create_rectangle_Not_equal(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_creat_new_Rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 89)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_Square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_Square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_Square_Not_equal(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class Test_Load_From_File(unittest.TestCase):
    """Test cases for load_from_file method of Base class"""
    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_1_Rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        list_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_output[0]))

    def test_load_from_file_2_Rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(5, 1, 3, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 5)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_output[0]))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_output[0]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)
