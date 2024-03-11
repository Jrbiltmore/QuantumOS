import os
import time
import subprocess

class PowerUsageMonitor:
    def __init__(self):
        self.battery_path = "/sys/class/power_supply/BAT0/"
        self.check_battery_exists()

    def check_battery_exists(self):
        if not os.path.exists(self.battery_path):
            raise FileNotFoundError("Battery information not available.")

    def read_battery_capacity(self):
        with open(os.path.join(self.battery_path, "capacity"), "r") as file:
            capacity = file.read().strip()
        return int(capacity)

    def read_power_draw(self):
        with open(os.path.join(self.battery_path, "current_now"), "r") as file:
            current_now = file.read().strip()
        with open(os.path.join(self.battery_path, "voltage_now"), "r") as file:
            voltage_now = file.read().strip()
        power_draw = (int(current_now) * int(voltage_now)) / 1_000_000_000_000  # Convert to Watts
        return power_draw

    def monitor_power_usage(self, interval=5):
        try:
            while True:
                capacity = self.read_battery_capacity()
                power_draw = self.read_power_draw()
                print(f"Battery Capacity: {capacity}% - Power Draw: {power_draw:.2f}W")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Monitoring stopped.")

if __name__ == "__main__":
    monitor = PowerUsageMonitor()
    monitor.monitor_power_usage()
