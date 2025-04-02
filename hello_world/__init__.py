"""
Hello World package for cloud builds and git hooks.
"""

from ._version import __version__


def say_hello(name: str = "World") -> str:
    """
    Return a greeting message.
    """
    return f"Hello, {name}!"
