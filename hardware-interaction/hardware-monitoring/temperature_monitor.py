import os
import time

class TemperatureMonitor:
    def __init__(self, thermal_zone=0):
        self.thermal_zone_path = f"/sys/class/thermal/thermal_zone{thermal_zone}/"

    def check_thermal_zone_exists(self):
        if not os.path.exists(self.thermal_zone_path):
            raise FileNotFoundError("Thermal zone not found.")

    def read_temperature(self):
        self.check_thermal_zone_exists()
        with open(os.path.join(self.thermal_zone_path, "temp"), "r") as file:
            # Temperature is read in millidegree Celsius
            temperature_milli_celsius = int(file.read().strip())
        # Convert to Celsius
        temperature_celsius = temperature_milli_celsius / 1000.0
        return temperature_celsius

    def monitor_temperature(self, interval=5):
        try:
            while True:
                temperature_celsius = self.read_temperature()
                print(f"Current Temperature: {temperature_celsius:.2f}°C")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Temperature monitoring stopped.")

if __name__ == "__main__":
    # Initialize with the desired thermal zone, if different from default
    monitor = TemperatureMonitor()
    print("Starting temperature monitoring...")
    monitor.monitor_temperature()
