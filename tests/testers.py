"""
TkConsole Testers

This module contains unit tests for the TkConsole package. It tests the functionality of the Console class
and its methods using the unittest framework and mocking.

Classes:
    ConsoleTest (class): Unit tests for the Console class.

Usage:
    Run this module to execute the unit tests for the Console class.
"""

import os
import unittest
from unittest.mock import patch
import tkinter as tk
from TkConsole import Console


class ConsoleTest(unittest.TestCase):
    """
    ConsoleTest class

    This class contains unit tests for the Console class of the TkConsole package.

    Methods:
        setUp(self): Set up the test environment.
        test_print_output(self): Test the print method's output to the text area.
        test_input(self): Test the input method by mocking the built-in input function.
        test_copy_text(self): Test the copy_text method's functionality.
        test_paste_text(self): Test the paste_text method's functionality.
        tearDown(self): Clean up the test environment after each test.
    """

    def setUp(self):
        """
        Set up the test environment.

        This method creates a Tkinter root window and initializes a Console instance for testing.
        It also initializes attributes for accessing the text area, entry widget, and user_input_var.

        Returns:
            None
        """
        if os.name != "nt":
            os.system('Xvfb :1 -screen 0 1600x1200x16  &')
        os.environ["DISPLAY"] = ":1.0"
        self.root = tk.Tk()
        self.console = Console(self.root)
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
        if self.console:
            self.console.parent.destroy()

    def test_print_output(self):
        """
        Test the print method's output to the text area.

        This method tests whether the print method correctly inserts text into the text area.

        Returns:
            None
        """
        self.setUp()
        expected_output = "Hello, world! This terminal-like library is great.\n"
        self.console.print("Hello, world!", end=" ")
        self.console.print("This terminal-like library is great.")
        self.assertEqual(self.text_area.get("1.0", tk.END), expected_output)
        self.root.dooneevent()
        self.tearDown()

    def test_input(self):
        """
        Test the input method by mocking the built-in input function.

        This method uses the unittest.mock.patch decorator to mock the built-in input function,
        allowing for controlled input during testing.

        Returns:
            None
        """
        self.setUp()
        with patch("builtins.input", return_value="42"):
            user_input = self.console.input("Enter a number: ")
            self.assertEqual(user_input, "42")
        self.root.dooneevent()
        self.tearDown()

    def test_copy_text(self):
        """
        Test the copy_text method's functionality.

        This method tests whether the copy_text method correctly copies selected text from the text area to the
        clipboard.

        Returns:
            None
        """
        self.setUp()
        self.text_area.insert("1.0", "Copy this text.")
        self.text_area.tag_add(tk.SEL, "1.0", "1.10")
        self.console.copy_text()
        clipboard_text = self.console.parent.clipboard_get()
        self.assertEqual(clipboard_text, "Copy this ")
        self.root.dooneevent()
        self.tearDown()

    def test_paste_text(self):
        """
        Test the paste_text method's functionality.

        This method tests whether the paste_text method correctly pastes text from the clipboard to the entry widget.

        Returns:
            None
        """
        self.setUp()
        clipboard_text = "Pasted text."
        self.console.parent.clipboard_clear()
        self.console.parent.clipboard_append(clipboard_text)
        self.console.input()
        self.console.paste_text()
        self.assertEqual(self.entry.get(), clipboard_text)
        self.root.dooneevent()
        self.tearDown()


if __name__ == '__main__':
    unittest.main()
