import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

class UnrealEngineWrapper:
    def __init__(self, root):
        self.root = root
        self.root.title("Unreal Engine Wrapper for QuantumOS")
        self.setup_ui()

    def setup_ui(self):
        self.open_project_btn = tk.Button(self.root, text="Open Unreal Project", command=self.open_unreal_project)
        self.open_project_btn.pack(pady=10)

        self.create_project_btn = tk.Button(self.root, text="Create New Unreal Project", command=self.create_unreal_project)
        self.create_project_btn.pack(pady=10)

        self.compile_project_btn = tk.Button(self.root, text="Compile Unreal Project", command=self.compile_unreal_project)
        self.compile_project_btn.pack(pady=10)

    def open_unreal_project(self):
        project_file = filedialog.askopenfilename(title="Select Unreal Project File", filetypes=[("Unreal Project", "*.uproject")])
        if project_file:
            try:
                subprocess.run(["path/to/UnrealEditor", project_file], check=True)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to open Unreal project: {e}")
            except FileNotFoundError:
                messagebox.showerror("Error", "Unreal Engine executable not found. Please ensure Unreal Engine is installed.")

    def create_unreal_project(self):
        messagebox.showinfo("Info", "Creating new Unreal projects is not supported directly via this script. Please use Unreal Engine.")
        # Unreal Engine projects are typically created within the Unreal Editor due to the complexity and options required.

    def compile_unreal_project(self):
        project_dir = filedialog.askdirectory(title="Select Unreal Project Directory")
        if project_dir:
            try:
                subprocess.run(["path/to/UnrealBuildTool", "Development Win64 -Project=" + project_dir], check=True)
                messagebox.showinfo("Success", "Project compiled successfully.")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to compile Unreal project: {e}")
            except FileNotFoundError:
                messagebox.showerror("Error", "UnrealBuildTool not found. Please ensure Unreal Engine is installed and paths are correct.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnrealEngineWrapper(root)
    root.mainloop()
