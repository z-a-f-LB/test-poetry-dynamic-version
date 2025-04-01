"""
Test module for version utilities.
"""
import subprocess
from unittest.mock import patch

from hello_world.version import get_version, get_version_from_git


def test_get_version_from_git_with_tag():
    """Test getting version from git tag when tag exists."""
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = "v1.2.3-0-g1234567\n"
        mock_run.return_value.returncode = 0

        version_info = get_version_from_git()
        assert version_info == ("v1.2.3", 0)

        mock_run.assert_called_once_with(
            ["git", "describe", "--tags", "--long"],
            capture_output=True,
            text=True,
            check=True,
        )


def test_get_version_from_git_with_distance():
    """Test getting version from git tag with distance."""
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = "v1.2.3-2-g1234567\n"
        mock_run.return_value.returncode = 0

        version_info = get_version_from_git()
        assert version_info == ("v1.2.3", 2)


def test_get_version_from_git_no_tag():
    """Test getting version from git tag when no tag exists."""
    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = subprocess.CalledProcessError(1, ["git"])

        version_info = get_version_from_git()
        assert version_info is None


def test_get_version_with_git_tag():
    """Test get_version when git tag exists."""
    with patch("hello_world.version.get_version_from_git") as mock_get_git_version:
        mock_get_git_version.return_value = ("v1.2.3", 0)

        version = get_version()
        assert version == "v1.2.3"


def test_get_version_with_distance():
    """Test get_version when commits exist after tag."""
    with patch("hello_world.version.get_version_from_git") as mock_get_git_version:
        mock_get_git_version.return_value = ("v1.2.3", 2)

        version = get_version()
        assert version == "v1.2.3+2"


def test_get_version_without_git_tag():
    """Test get_version when no git tag exists."""
    with patch("hello_world.version.get_version_from_git") as mock_get_git_version:
        mock_get_git_version.return_value = None

        version = get_version()
        assert version == "0.1.0"