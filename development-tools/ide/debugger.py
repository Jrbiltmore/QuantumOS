import tkinter as tk
from tkinter import simpledialog

class SimpleDebugger:
    def __init__(self, code):
        self.code_lines = code.split("\n")
        self.breakpoints = set()
        self.current_line = 0
        self.locals = {}

    def set_breakpoint(self, line_number):
        self.breakpoints.add(line_number)

    def run(self):
        while self.current_line < len(self.code_lines):
            if self.current_line in self.breakpoints:
                print(f"Breakpoint hit at line {self.current_line + 1}")
                self.debug_prompt()
            try:
                exec(self.code_lines[self.current_line], globals(), self.locals)
            except Exception as e:
                print(f"Error on line {self.current_line + 1}: {e}")
                break
            self.current_line += 1

    def debug_prompt(self):
        command = simpledialog.askstring("Debug Prompt", "Enter command (n: next, c: continue, v: vars):")
        if command == "n":
            return
        elif command == "c":
            self.breakpoints.remove(self.current_line)
        elif command == "v":
            print(self.locals)
            self.debug_prompt()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    # Sample code to debug
    code = """
x = 10
y = 0
for i in range(5):
    y += x
    x -= 1
print(y)
"""
    debugger = SimpleDebugger(code)
    debugger.set_breakpoint(3)  # Set a breakpoint on the loop start
    debugger.run()
