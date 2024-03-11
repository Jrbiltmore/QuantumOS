import dbus
from dbus.mainloop.glib import DBusGMainLoop
import glib

class BluetoothDriver:
    def __init__(self):
        self.bus = dbus.SystemBus()
        self.adapter_path = self._get_adapter_path()
        self.adapter = dbus.Interface(self.bus.get_object('org.bluez', self.adapter_path), 'org.bluez.Adapter1')

    def _get_adapter_path(self):
        """Discover the default Bluetooth adapter's D-Bus path."""
        remote_om = dbus.Interface(self.bus.get_object('org.bluez', '/'), 'org.freedesktop.DBus.ObjectManager')
        objects = remote_om.GetManagedObjects()
        for o, props in objects.items():
            if 'org.bluez.Adapter1' in props.keys():
                return o
        raise Exception("Bluetooth adapter not found")

    def start_discovery(self):
        """Start the Bluetooth discovery process to find devices."""
        self.adapter.StartDiscovery()
        print("Discovery started")

    def stop_discovery(self):
        """Stop the Bluetooth discovery process."""
        self.adapter.StopDiscovery()
        print("Discovery stopped")

    def list_devices(self):
        """List discovered Bluetooth devices."""
        remote_om = dbus.Interface(self.bus.get_object('org.bluez', '/'), 'org.freedesktop.DBus.ObjectManager')
        objects = remote_om.GetManagedObjects()
        devices = []
        for o, props in objects.items():
            if 'org.bluez.Device1' in props.keys():
                devices.append(o)
        return devices

if __name__ == "__main__":
    DBusGMainLoop(set_as_default=True)
    driver = BluetoothDriver()
    driver.start_discovery()
    try:
        loop = glib.MainLoop()
        loop.run()
    except KeyboardInterrupt:
        driver.stop_discovery()
        print("Devices discovered:")
        for device in driver.list_devices():
            print(device)
