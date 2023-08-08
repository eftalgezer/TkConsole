# TkConsole
[![PyPI version](https://badge.fury.io/py/TkConsole.svg)](https://badge.fury.io/py/TkConsole)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/TkConsole.svg)](https://pypi.python.org/pypi/TkConsole/)
[![Python package](https://github.com/eftalgezer/TkConsole/actions/workflows/python-package.yml/badge.svg)](https://github.com/eftalgezer/TkConsole/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/eftalgezer/TkConsole/branch/main/graph/badge.svg?token=Q9TJFIN1U1)](https://codecov.io/gh/eftalgezer/TkConsole)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/9f587291fa574f638dba71241657902b)](https://app.codacy.com/gh/eftalgezer/TkConsole/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)
[![PyPI download month](https://img.shields.io/pypi/dm/TkConsole.svg)](https://pypi.python.org/pypi/TkConsole/)
[![PyPI download week](https://img.shields.io/pypi/dw/TkConsole.svg)](https://pypi.python.org/pypi/TkConsole/)
[![PyPI download day](https://img.shields.io/pypi/dd/TkConsole.svg)](https://pypi.python.org/pypi/TkConsole/)
![GitHub all releases](https://img.shields.io/github/downloads/eftalgezer/TkConsole/total?style=flat)
[![GitHub contributors](https://img.shields.io/github/contributors/eftalgezer/TkConsole.svg)](https://github.com/eftalgezer/TkConsole/graphs/contributors/)
[![CodeFactor](https://www.codefactor.io/repository/github/eftalgezer/TkConsole/badge)](https://www.codefactor.io/repository/github/eftalgezer/TkConsole)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9f587291fa574f638dba71241657902b)](https://app.codacy.com/gh/eftalgezer/TkConsole/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![PyPI license](https://img.shields.io/pypi/l/TkConsole.svg)](https://pypi.python.org/pypi/TkConsole/)

<p align="center">
![TkConsole Screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQ5AhNaTawdxrkYtJWltKRA_wgHmPuJ4YavwVNsGOwfrlaXxxFDbHnQPReGFyb9Vu8jEjONXy8YFjz-2EYdH5LM_1tLo5HwKqCDh3C7wtab9aRyURy_OlOKWvZ4Y9-L3NHh0Hr8pWzY8z-3mN-Kwxrt_CRXyKwq7nKvuYM0fKn9wTig6uap8R3SzC5y2KU/s1600/tkconsole_example.png)
</p>

TkConsole is a Python library that provides a customizable terminal-like console widget using the Tkinter GUI framework.

## Installation

TkConsole can be installed using pip:

```bash
pip install SIESTAstepper

# to make sure you have the latest version
pip install -U SIESTAstepper

# latest available code base
pip install -U git+https://github.com/eftalgezer/TkConsole.git
```

## Tutorial

[Building an interactive console interface with TkConsole](https://beyondthearistotelian.blogspot.com/2023/08/building-interactive-console-interface.html)

## Usage

To use TkConsole in your Python application, you can follow these steps:

```python
import tkinter as tk
from TkConsole import Console

root = tk.Tk()
console = Console(root)
console.pack(expand=True, fill="both")

console.print("Hello, world!")
user_input = console.input("Enter something: ")
console.print(f"You entered: {user_input}")

root.mainloop()
```
## Features

- Customizable font, background, and foreground colors 
- Printing text to the console 
- Taking user input 
- Copy and paste functionality

## Unit Tests

TkConsole comes with a comprehensive set of unit tests to ensure its functionality. To run the tests, navigate to the tests directory and execute tests.py:

```bash
cd tests
python tests.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU General Public License v3.0](https://github.com/eftalgezer/TkConsole/blob/master/LICENSE) 
