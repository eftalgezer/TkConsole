# Example: Creating Custom Commands in TkConsole

In this example, we will explore how to create and use custom commands in TkConsole. Custom commands allow you to define specific actions that users can execute within the console interface.

## Getting Started

Let's start by setting up a basic Tkinter application with TkConsole:

```python
import tkinter as tk
from TkConsole import Console

def custom_command(command):
    if command == "hello":
        console.print("Hello, world!")
    else:
        console.print("Invalid command.")

root = tk.Tk()
console = Console(root)

console.print("Welcome to TkConsole!")
while True:
    user_input = console.input("Enter a command: ")
    if user_input == "exit":
        break
    custom_command(user_input)

root.mainloop()
```

This code initializes a Tkinter window and embeds a TkConsole widget within it. It also defines a custom_command function that takes a command as an argument and performs specific actions based on the command.

## Using Custom Commands

With the custom command function defined, you can manually call it by passing the desired command as an argument:

```python
custom_command("hello")
```

When you run this code, the console will print:

```
Hello, world!
```
You can modify the argument to test the "Invalid command" response:

```python
custom_command("unknown")
```

The console will respond with:

```
Invalid command.
```

## Extending Custom Commands

To extend your custom commands, simply define more functions and call them with different command names. You can implement complex logic and interactions, making your console more powerful and interactive.

## Conclusion

Creating custom commands in TkConsole is straightforward. By defining functions that take specific command arguments, you can add versatile interactivity to your Tkinter applications. This example demonstrates a basic implementation, but you can expand upon it to create more advanced command systems that suit your application's needs.
