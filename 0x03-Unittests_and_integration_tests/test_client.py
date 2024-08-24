#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Arrange: Define a sample return value for get_json
        mock_return_value = {"login": org_name, "id": 12345}
        mock_get_json.return_value = mock_return_value

        # Act: Instantiate the GithubOrgClient and call the org property
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert: Verify get_json is called once with the correct URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        # Assert: Check that the org method returns the mocked JSON
        self.assertEqual(result, mock_return_value)


if __name__ == '__main__':
    unittest.main()
