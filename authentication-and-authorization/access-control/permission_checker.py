import os
import sys

def check_permissions(path):
    """
    Check read, write, and execute permissions for the given path.
    Returns a dictionary with boolean values for each permission.
    """
    permissions = {
        'read': os.access(path, os.R_OK),
        'write': os.access(path, os.W_OK),
        'execute': os.access(path, os.X_OK)
    }
    return permissions

def report_permissions(path):
    """
    Reports the permissions of the given path to the console.
    """
    permissions = check_permissions(path)
    print(f"Permissions for {path}:")
    for perm, has_perm in permissions.items():
        print(f"  {perm.capitalize()}: {'Yes' if has_perm else 'No'}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python permission_checker.py <path>")
        sys.exit(1)

    path = sys.argv[1]
    report_permissions(path)
