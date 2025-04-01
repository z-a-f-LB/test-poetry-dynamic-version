"""
Test module for hello_world package.
"""
from hello_world import say_hello


def test_say_hello_default():
    """Test the say_hello function with default parameter."""
    assert say_hello() == "Hello, World!"


def test_say_hello_custom():
    """Test the say_hello function with custom name."""
    assert say_hello("Alice") == "Hello, Alice!"