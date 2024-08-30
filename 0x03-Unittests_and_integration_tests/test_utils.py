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
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """Unit tests for the get_json function from the utils module.

        This class tests the get_json function to ensure it
            returns the expected JSON payload when making an HTTP GET
                request to a specified URL.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests.get')
    def test_get_json(self, url, test_payload, mock):
        """
            Test that get_json returns the expected JSON payload.

            Args:
                url (str): The URL to make the GET request to.
                test_payload (dict): The expected JSON payload.
                mock (Mock): The mocked requests.get function.

            Asserts:
                The mocked requests.get method was called
                    exactly once with the test_url.
                The output of get_json is equal to
                    the expected test_payload.
        """
        response = Mock()
        response.json.return_value = test_payload
        mock.return_value = response

        self.assertEqual(get_json(url), test_payload)
        mock.assert_called_once_with(url)


if __name__ == '__main__':
    unittest.main()
