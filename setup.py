"""
Setup file for TkConsole
"""
import os
from setuptools import setup
import io

HERE = os.path.dirname(os.path.abspath(__file__))

LONG_DESCRIPTION = None

with io.open(os.path.join(HERE, "README.md"), "r", encoding="utf-8") as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name="TkConsole",
    version="0.1.0",
    description="TkConsole is a custom console widget for Tkinter, providing a terminal-like interface for text "
                "output, user input, and copy/paste operations.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/eftalgezer/TkConsole",
    author="Eftal Gezer",
    author_email="eftal.gezer@astrobiyoloji.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Utilities",
        "Typing :: Typed",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="TkConsole, custom console, Tkinter console, terminal-like interface, Python GUI, text input, "
             "text output, copy and paste, scrolledtext",
    packages=["TkConsole"],
    install_requires=[],
    project_urls={
        "Bug Reports": "https://github.com/eftalgezer/TkConsole/issues",
        "Source": "https://github.com/eftalgezer/TkConsole/",
        "Blog": "https://beyondthearistotelian.blogspot.com/search/label/TkConsole",
        "Developer": "https://www.eftalgezer.com/",
    },
)
