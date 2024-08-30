#!/usr/bin/env python3
"""
    Unit tests for the access_nested_map function from the utils module.

    This module uses the unittest framework along with parameterized testing
        to validate the behavior of the access_nested_map function, which
        retrieves values from nested dictionaries using a specified path.

    Classes:
        TestAccessNestedMap: Defines test cases for
            the access_nested_map function.

    Functions:
        test_access_nested_map(nested_map, path, expected):
            Tests that access_nested_map returns the correct
            value from the nested map based on the provided path.
"""

import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function from the utils module.

        The tests validate that the function correctly retrieves values
            from nested dictionaries given a specific path.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map correctly retrieves the
            value from the nested map based on the provided path.

            Args:
                nested_map (dict): The nested dictionary to search.
                path (tuple): A tuple representing the path to the
                    value in the nested dictionary.
                expected: The expected value at the specified path.

            Asserts:
                The value returned by access_nested_map
                    matches the expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b'))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises a KeyError
            when the path does not exist in the nested map.

        Args:
            nested_map (dict): The nested dictionary to search.
            path (tuple): A tuple representing the path to
                the value in the nested dictionary.

        Asserts:
            A KeyError is raised when access_nested_map is called
                with a path that does not exist in the nested dictionary.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
