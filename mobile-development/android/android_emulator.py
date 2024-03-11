import subprocess
import os

EMULATOR_PATH = "/path/to/android/sdk/emulator"  # Update this path
AVD_NAME = "Your_AVD_Name"  # Update this with the name of your Android Virtual Device
APK_PATH = "/path/to/your/app.apk"  # Update this with the path to your APK

def start_emulator():
    """Starts the Android emulator."""
    subprocess.run([os.path.join(EMULATOR_PATH, "emulator"), "-avd", AVD_NAME], check=True)

def install_apk():
    """Installs an APK on the emulator."""
    subprocess.run(["adb", "install", APK_PATH], check=True)

def take_screenshot():
    """Takes a screenshot from the emulator."""
    screenshot_path = os.path.join(os.getcwd(), "emulator_screenshot.png")
    subprocess.run(["adb", "exec-out", "screencap", "-p", ">", screenshot_path], shell=True, check=True)
    print(f"Screenshot saved to {screenshot_path}")

def main():
    # Example usage
    print("Starting emulator...")
    start_emulator()
    print("Installing APK...")
    install_apk()
    print("Taking a screenshot...")
    take_screenshot()

if __name__ == "__main__":
    main()
