"""
TkConsole Test Patches

This module provides fake classes to patch certain Tkinter classes for testing purposes.
These fake classes allow for mocking the behavior of Tkinter's classes during unit tests.

Classes:
    FakeTk (class): A fake Tkinter root window class for testing.
    FakeScrolledText (class): A fake ScrolledText class for testing.

Usage:
    These fake classes are used in unit tests to mock the behavior of Tkinter classes and methods,
    ensuring that the unit tests are isolated and independent of the actual Tkinter functionality.
"""

import tkinter as tk
from tkinter import scrolledtext


class FakeTk(tk.Tk):
    """
    FakeTk class

    This class provides a fake implementation of the Tkinter root window class for testing purposes.

    Methods:
        mainloop(self, **kwargs): Mocks the mainloop method of Tkinter's root window.
    """
    def __init__(self):
        """
        Initialize a fake Tkinter root window for testing purposes.

        Returns:
            None
        """
        super().__init__()

    def mainloop(self, n: int = ...) -> None:
        """
        Mocks the mainloop method of Tkinter's root window.

        Args:
            n (int): Number of iterations (ignored).

        Returns:
            None
        """

    class Entry(tk.Entry):
        """
        Fake Entry class

        This class provides a fake implementation of the Entry widget for testing purposes.

        Methods:
            mainloop(self, n: int = ...) -> None: Mocks the mainloop method of Tkinter's Entry widget.
        """
        def __init__(self):
            """
            Initialize a fake Entry widget for testing purposes.

            Returns:
                None
            """
            super().__init__()

        def mainloop(self, n: int = ...) -> None:
            """
            Mocks the mainloop method of Tkinter's Entry widget.

            Args:
                n (int): Number of iterations (ignored).

            Returns:
                None
            """


class FakeScrolledText(scrolledtext.ScrolledText):
    """
    FakeScrolledText class

    This class provides a fake implementation of the ScrolledText class for testing purposes.

    Methods:
        mainloop(self, n: int = ...) -> None: Mocks the mainloop method of Tkinter's ScrolledText.
        winfo_height(self) -> int: Mocks the winfo_height method of Tkinter's ScrolledText.
    """
    def __init__(self, master=None, **kw):
        """
        Initialize a fake ScrolledText widget for testing purposes.

        Args:
            master: The master widget (ignored).
            **kw: Additional keyword arguments (ignored).

        Returns:
            None
        """
        super().__init__()

    def mainloop(self, n: int = ...) -> None:
        """
        Mocks the mainloop method of Tkinter's ScrolledText.

        Args:
            n (int): Number of iterations (ignored).

        Returns:
            None
        """

    def winfo_height(self) -> int:
        """
        Mocks the winfo_height method of Tkinter's ScrolledText.

        Returns:
            int: Height of the ScrolledText.
        """
        return 500
