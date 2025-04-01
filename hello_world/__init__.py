"""
Hello World package for cloud builds and git hooks.
"""

try:
    from ._version import __version__
except ImportError:
    __version__ = "0.0.0+placeholder"


def say_hello(name: str = "World") -> str:
    """
    Return a greeting message.
    """
    return f"Hello, {name}!"
