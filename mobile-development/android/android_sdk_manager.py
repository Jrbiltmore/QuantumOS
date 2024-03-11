import subprocess
import sys

# Path to the Android SDK's sdkmanager. Update this if necessary.
SDKMANAGER_PATH = "sdkmanager"  # Assuming sdkmanager is in the system's PATH

def list_packages():
    """Lists all available packages."""
    subprocess.run([SDKMANAGER_PATH, "--list"], check=True)

def install_package(package_name):
    """Installs a specified package."""
    subprocess.run([SDKMANAGER_PATH, package_name], check=True)

def update_all_packages():
    """Updates all installed packages."""
    subprocess.run([SDKMANAGER_PATH, "--update"], check=True)

def main():
    if len(sys.argv) < 2:
        print("Usage: python android_sdk_manager.py [list|install|update] [package_name]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        list_packages()
    elif command == "install":
        if len(sys.argv) != 3:
            print("Please specify a package name to install.")
            sys.exit(1)
        package_name = sys.argv[2]
        install_package(package_name)
    elif command == "update":
        update_all_packages()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
