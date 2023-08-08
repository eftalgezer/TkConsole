"""
TkConsole Testers

This module contains unit tests for the TkConsole package. It tests the functionality of the Console class
and its methods using the unittest framework and mocking.

Classes:
    ConsoleTester (class): Unit tests for the Console class.
"""

import os
from subprocess import Popen
import unittest
from unittest.mock import patch
import tkinter as tk
from TkConsole import Console
from .patches import FakeTk, FakeScrolledText


class ConsoleTester(unittest.TestCase):
    """
    ConsoleTester class

    This class contains unit tests for the Console class of the TkConsole package.

    Methods:
        setUp(self): Set up the test environment.
        tearDown(self): Clean up the test environment after each test.
        print_tester(self, prints=None, expected_output=None): Tester function for the print method's output to the text
        area.
        input_tester(self, prompt=None, return_value=None): Tester function for the input method by mocking the built-in
        input function.
        copy_text_tester(self, text=None, text_to_copy=None, tag_start=None, tag_end=None): Tester function for the
        copy_text method's functionality.
        paste_text_tester(self, clipboard_text): Tester function for the paste_text method's functionality.
    """

    def setUp(self):
        """
        Set up the test environment.

        This method creates a Tkinter root window and initializes a Console instance for testing.
        It also initializes attributes for accessing the text area, entry widget, and user_input_var.

        Returns:
            None
        """
        if os.name != "nt" and os.getenv("GITHUB_ACTIONS"):
            Popen(["/usr/bin/Xvfb", ":1", "-screen", "0", "1600x1200x16", "&"])
            os.environ["DISPLAY"] = ":1.0"
        self.root = FakeTk()
        self.console = Console(self.root)
        self.console.text_area = FakeScrolledText(
            self.console.parent, wrap=tk.WORD, font=self.console.font, background=self.console.background,
            foreground=self.console.foreground, padx=0,
            pady=0, borderwidth=0, border=0.0, insertborderwidth=0, selectborderwidth=0
        )
        self.text_area = self.console.text_area
        self.entry = self.console.entry
        self.user_input_var = self.console.user_input_var

    def tearDown(self):
        """
        Clean up the test environment after each test.

        This method ensures that the Tkinter root window is destroyed after each test case,
        preventing any graphical artifacts or interference between test cases.

        Returns:
            None
        """
        if self.root:
            self.root.destroy()

    def print_tester(self, prints=None, expected_output=None):
        """
        Tester function for the print method's output to the text area.

        This method tests whether the print method correctly inserts text into the text area.

        Returns:
            None
        """
        self.setUp()
        for item in prints:
            if item[1]:
                self.console.print(item[0], end=item[1])
            else:
                self.console.print(item[0])
        self.assertEqual(self.text_area.get("1.0", tk.END), expected_output)
        self.root.update_idletasks()
        self.tearDown()
        self.root = None

    def input_tester(self, prompt=None, return_value=None):
        """
        Tester function for the input method by mocking the built-in input function.

        This method uses the unittest.mock.patch decorator to mock the built-in input function,
        allowing for controlled input during testing.

        Returns:
            None
        """
        self.setUp()
        with patch("builtins.input", return_value=return_value):
            user_input = self.console.input(prompt)
            self.assertEqual(user_input, return_value)
        self.root.update_idletasks()
        self.tearDown()
        self.root = None

    def copy_text_tester(self, text=None, text_to_copy=None, tag_start=None, tag_end=None):
        """
        Tester function for the copy_text method's functionality.

        This method tests whether the copy_text method correctly copies selected text from the text area to the
        clipboard.

        Returns:
            None
        """
        self.setUp()
        self.text_area.insert(tag_start, text)
        self.text_area.tag_add(tk.SEL, tag_start, tag_end)
        self.console.copy_text()
        clipboard_text = self.console.parent.clipboard_get()
        self.assertEqual(clipboard_text, text_to_copy)
        self.root.update_idletasks()
        self.tearDown()
        self.root = None

    def paste_text_tester(self, clipboard_text):
        """
        Tester function for the paste_text method's functionality.

        This method tests whether the paste_text method correctly pastes text from the clipboard to the entry widget.

        Returns:
            None
        """
        self.setUp()
        self.console.parent.clipboard_clear()
        self.console.parent.clipboard_append(clipboard_text)
        self.console.input()
        self.console.paste_text()
        self.assertEqual(self.entry.get(), clipboard_text)
        self.root.update_idletasks()
        self.tearDown()
        self.root = None
