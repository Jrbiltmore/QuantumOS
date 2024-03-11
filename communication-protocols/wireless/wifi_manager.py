import subprocess
import re

def scan_wifi_networks():
    """Scan for available WiFi networks."""
    try:
        result = subprocess.check_output(["nmcli", "-f", "SSID,SECURITY", "dev", "wifi"], universal_newlines=True)
        print("Available WiFi networks:")
        print(result)
    except subprocess.CalledProcessError as e:
        print("Failed to scan WiFi networks:", e)

def connect_to_wifi(ssid, password):
    """Connect to a WiFi network with the given SSID and password."""
    try:
        # Attempt to add a WiFi connection
        add_conn = subprocess.run(["nmcli", "dev", "wifi", "connect", ssid, "password", password], check=True, stdout=subprocess.PIPE, universal_newlines=True)
        print(add_conn.stdout)
    except subprocess.CalledProcessError as e:
        print("Failed to connect to WiFi network:", e)

def list_connections():
    """List existing WiFi connections."""
    try:
        result = subprocess.check_output(["nmcli", "con", "show"], universal_newlines=True)
        print("Existing connections:")
        print(result)
    except subprocess.CalledProcessError as e:
        print("Failed to list connections:", e)

def disconnect_wifi():
    """Disconnect the current WiFi connection."""
    try:
        subprocess.run(["nmcli", "dev", "disconnect", "wlan0"], check=True, stdout=subprocess.PIPE, universal_newlines=True)
        print("Disconnected from WiFi.")
    except subprocess.CalledProcessError as e:
        print("Failed to disconnect WiFi:", e)

# Example usage
if __name__ == '__main__':
    scan_wifi_networks()
    # Connect to a network (fill in with your SSID and password)
    # connect_to_wifi('YourSSID', 'YourPassword')
    list_connections()
    # Disconnect current WiFi
    # disconnect_wifi()
