#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the correct URL"""
        # Arrange: Define a sample return value for the org property
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }

        # Act: Instantiate the client and access the _public_repos_url property
        client = GithubOrgClient("test_org")
        result = client._public_repos_url

        # Assert: Verify the _public_repos_url returns the expected repos_url
        expected_url = "https://api.github.com/orgs/test_org/repos"
        self.assertEqual(result, expected_url)

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test that public_repos returns the correct list of repos"""
        # Define a mock payload to be returned by get_json
        mock_payload = [
            {"name": "repo1", "license": {"key": "my_license"}},
            {"name": "repo2", "license": {"key": "other_license"}},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = mock_payload

        # Set the return value of the mocked _public_repos_url property
        mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"
            
        # Instantiate the GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call public_repos method
        result = client.public_repos()

        # Check that the result is as expected
        expected_repos = ["repo1", "repo2", "repo3"]
        self.assertEqual(result, expected_repos)

        # Check that the mocked property and get_json were called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/test_org/repos")
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
        ({"license": {}}, "my_license", False),
        ({"license": {"key": None}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the correct boolean"""
        # Call the has_license method
        result = GithubOrgClient.has_license(repo, license_key)

        # Assert that the result matches the expected value
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
