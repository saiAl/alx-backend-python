#!/usr/bin/env python3
""" """
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, url, mock_get_json):
        """Test that the GithubOrgClient.org method returns the correct value.

            Args:
                org_name (str): The organization name to test.
                url (str): The URL that get_json is expected to be called with.
                mock_get_json (Mock): The mock object for get_json.

            Asserts:
                The get_json function is called once with the expected URL.
                The org method returns the mocked data.
        """
        response = {
                "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
                }
        mock_get_json.return_value = response
        client = GithubOrgClient(org_name)

        self.assertEqual(client.org, response)

        mock_get_json.assert_called_once()
