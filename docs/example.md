# Example

Here's a basic example of how to create a TkConsole widget and use its features:

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