"""
TkConsole Unit Tests

This module contains unit tests for the TkConsole library. It tests various functionalities of the Console class to
ensure that they work as expected. The tests cover printing output, taking user input, copying and pasting text,
and other interactive features provided by the Console class.
"""

from .testers import ConsoleTester


def test_print():
    """
    Test the print method of the Console class.

    This function uses the ConsoleTester class to test the print method's output to the text area.

    Returns:
        None
    """
    tester = ConsoleTester()
    prints = [["Hello, world!", " "], ["This terminal-like library is great.", None]]
    tester.print_tester(prints=prints, expected_output="Hello, world! This terminal-like library is great.\n")


def test_input():
    """
    Test the input method of the Console class.

    This function uses the ConsoleTester class to test the input method by mocking the built-in input function.

    Returns:
        None
    """
    tester = ConsoleTester()
    tester.input_tester(prompt="Enter a number: ", return_value="42")


def test_copy_text():
    """
    Test the copy_text method of the Console class.

    This function uses the ConsoleTester class to test the copy_text method's functionality.

    Returns:
        None
    """
    tester = ConsoleTester()
    tester.copy_text_tester(text="Copy this text.", text_to_copy="Copy this ", tag_start="1.0", tag_end="1.10")


def test_paste_text():
    """
    Test the paste_text method of the Console class.

    This function uses the ConsoleTester class to test the paste_text method's functionality.

    Returns:
        None
    """
    tester = ConsoleTester()
    tester.paste_text_tester(clipboard_text="Pasted text.")
