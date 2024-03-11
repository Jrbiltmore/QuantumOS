import subprocess
import os
import sys

# Define paths
project_root = os.path.dirname(os.path.abspath(__file__))
c_components_path = os.path.join(project_root, 'c_components')
python_components_path = os.path.join(project_root, 'python_components')

# Function to compile C components
def compile_c_components():
    print("Compiling C components...")
    make_process = subprocess.run(['make'], cwd=c_components_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if make_process.returncode == 0:
        print("C components compiled successfully.")
    else:
        print("Error compiling C components:")
        print(make_process.stderr.decode())
        sys.exit(1)

# Function to set up Python environment
def setup_python_environment():
    print("Setting up Python environment...")
    requirements_path = os.path.join(project_root, 'requirements.txt')
    pip_process = subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', requirements_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if pip_process.returncode == 0:
        print("Python environment set up successfully.")
    else:
        print("Error setting up Python environment:")
        print(pip_process.stderr.decode())
        sys.exit(1)

# Function to verify Qiskit, Cirq, and pyQuil installation
def verify_dependencies():
    print("Verifying quantum computing library dependencies...")
    try:
        import qiskit
        import cirq
        import pyquil
        print("All dependencies are correctly installed.")
    except ImportError as e:
        print(f"Dependency error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    compile_c_components()
    setup_python_environment()
    verify_dependencies()
    print("Project build and setup completed successfully.")
