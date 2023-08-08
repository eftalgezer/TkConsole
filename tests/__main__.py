"""
TkConsole Test Suite

This module serves as the entry point for running the TkConsole test suite. It executes the `test_by_threads` function
from the `thread.py` module to run all the test functions concurrently in separate threads.

Functions:
    main(): Entry point for running the TkConsole test suite.

Usage:
    Run this module to execute all the test functions concurrently using separate threads.
"""

from .thread import test_by_threads


def main():
    """
    Entry point for running the TkConsole test suite.

    This function executes the `test_by_threads` function from the `thread.py` module to run all the test functions
    concurrently using separate threads.

    Returns:
        None
    """
    test_by_threads()


if __name__ == "__main__":
    main()
