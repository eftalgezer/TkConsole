# Usage

To use TkConsole in your Tkinter-based projects, follow these steps:

1. Import the necessary modules:

```python
import tkinter as tk
from TkConsole import Console
```

Create a Tkinter window:

```python
root = tk.Tk()
```

Add a TkConsole widget to the window:

```python
console = Console(root)
console.pack(expand=True, fill="both")
```

Use the console's methods to interact with the user:

```python
console.print("Hello, world!")
user_input = console.input("Enter something: ")
console.print(f"You entered: {user_input}")
```

Start the Tkinter main loop:

```python
root.mainloop()
```

Feel free to customize the appearance and behavior of the console to suit your needs.
