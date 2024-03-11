import subprocess
import sys

# Utility function to run shell commands
def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"Error executing command: {' '.join(command)}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout.strip()

# Start a specific simulator
def start_simulator(device_id):
    run_command(f"xcrun simctl boot {device_id}")

# Install an app on the simulator
def install_app(device_id, app_path):
    run_command(f"xcrun simctl install {device_id} {app_path}")

# Take a screenshot
def take_screenshot(device_id, save_path):
    run_command(f"xcrun simctl io {device_id} screenshot {save_path}")

# Main function to demonstrate usage
def main():
    device_id = "YOUR_DEVICE_ID"  # Replace with your simulator's device ID
    app_path = "/path/to/your/app.app"  # Replace with the path to your .app file
    save_path = "/path/to/save/screenshot.png"  # Replace with where to save the screenshot
    
    # Example usage
    print("Starting the simulator...")
    start_simulator(device_id)
    
    print("Installing the app...")
    install_app(device_id, app_path)
    
    print("Taking a screenshot...")
    take_screenshot(device_id, save_path)
    print(f"Screenshot saved to {save_path}")

if __name__ == "__main__":
    main()
