"""
TkConsole Package

This package provides a custom Tkinter-based console widget for creating terminal-like interfaces.

Meta:
    __title__ (str): The title of the package ("TkConsole").
    __author__ (str): The author of the package ("Eftal Gezer").
    __license__ (str): The license of the package ("GNU GPL v3").
    __copyright__ (str): The copyright year and author ("Copyright 2023, Eftal Gezer").
    __version__ (str): The version of the package ("0.1.0").

Modules:
    core (module): Contains the Console class for creating the custom console widget.
"""


from __future__ import absolute_import

# meta
__title__ = "TkConsole"
__author__ = "Eftal Gezer"
__license__ = "GNU GPL v3"
__copyright__ = "Copyright 2023, Eftal Gezer"
__version__ = "0.1.0"

from .core import Console
