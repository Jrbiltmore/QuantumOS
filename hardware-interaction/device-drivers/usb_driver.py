import usb.core
import usb.util

class USBDeviceDriver:
    def __init__(self, vendor_id, product_id):
        self.device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
        if self.device is None:
            raise ValueError("Device not found")

        # Detach kernel driver if necessary
        if self.device.is_kernel_driver_active(0):
            try:
                self.device.detach_kernel_driver(0)
            except usb.core.USBError as e:
                raise ValueError("Could not detach kernel driver: %s" % str(e))

        self.device.set_configuration()
        cfg = self.device.get_active_configuration()
        intf = cfg[(0,0)]

        self.endpoint_out = usb.util.find_descriptor(
            intf,
            # match the first OUT endpoint
            custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT
        )

        self.endpoint_in = usb.util.find_descriptor(
            intf,
            # match the first IN endpoint
            custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_IN
        )

        if self.endpoint_in is None or self.endpoint_out is None:
            raise ValueError("Could not find an endpoint")

    def write(self, data):
        self.endpoint_out.write(data)

    def read(self, size):
        return self.endpoint_in.read(size, timeout=2000)

if __name__ == "__main__":
    # Example Vendor ID and Product ID
    VENDOR_ID = 0x1234
    PRODUCT_ID = 0x5678

    driver = USBDeviceDriver(VENDOR_ID, PRODUCT_ID)
    print("Device initialized")

    # Example data to write (as bytes)
    data_to_write = b'Hello, USB!'
    driver.write(data_to_write)
    print("Data written to device")

    # Attempt to read response
    try:
        response = driver.read(64)  # Read up to 64 bytes
        print("Received response:", response)
    except usb.core.USBError as e:
        print("USB error:", e)
