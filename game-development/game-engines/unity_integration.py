import subprocess
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class UnityIntegration:
    def __init__(self, root):
        self.root = root
        self.root.title("Unity Integration for QuantumOS")
        self.create_ui()

    def create_ui(self):
        open_project_btn = tk.Button(self.root, text="Open Unity Project", command=self.open_unity_project)
        open_project_btn.pack(pady=20)
        
        create_project_btn = tk.Button(self.root, text="Create New Unity Project", command=self.create_unity_project)
        create_project_btn.pack(pady=20)

    def open_unity_project(self):
        project_path = filedialog.askdirectory(title="Select Unity Project Folder")
        if project_path:
            try:
                subprocess.run(["/path/to/Unity", "-projectPath", project_path], check=True)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to open Unity project: {e}")
            except FileNotFoundError:
                messagebox.showerror("Error", "Unity executable not found. Please ensure Unity is installed and the path is correct.")

    def create_unity_project(self):
        project_path = filedialog.askdirectory(title="Select folder for new Unity Project")
        project_name = simpledialog.askstring("Project Name", "Enter the name for the new Unity project:")
        if project_path and project_name:
            full_path = os.path.join(project_path, project_name)
            try:
                subprocess.run(["/path/to/Unity", "-createProject", full_path], check=True)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to create Unity project: {e}")
            except FileNotFoundError:
                messagebox.showerror("Error", "Unity executable not found. Please ensure Unity is installed and the path is correct.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnityIntegration(root)
    root.mainloop()
