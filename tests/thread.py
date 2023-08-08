"""
Testing with Threads

This module provides a mechanism for running test functions in separate threads. It defines a `thread` decorator
and a `test_by_threads` function that allows running multiple test functions concurrently in different threads.

Functions:
    thread(func): A decorator to run a test function in a separate thread.
    test_by_threads(): Run test functions concurrently using separate threads.
"""

import queue
import threading
from .tests import test_print, test_input, test_copy_text, test_paste_text


def thread(func):
    """
    A decorator to run a test function in a separate thread.

    Args:
        func (callable): The test function to be executed in a separate thread.

    Returns:
        None
    """
    func = globals()[func]
    func()


def test_by_threads():
    """
    Run test functions concurrently using separate threads.

    This function collects test functions defined in the `.tests` module, creates separate threads for each function,
    and runs them concurrently.

    Returns:
        None
    """
    funcs = [func for func in dir(".tests") if func.startswith("test_")]
    q = queue.Queue()
    threads = [threading.Thread(target=thread, args=(func, q)) for func in funcs]
    for th in threads:
        th.daemon = True
        th.start()
