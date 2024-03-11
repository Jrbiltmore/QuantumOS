import struct

class EthernetFrame:
    """
    A simple representation of an Ethernet frame.
    """
    def __init__(self, dest_mac, src_mac, payload, eth_type=0x0800):
        """
        Initialize the Ethernet frame with destination MAC, source MAC, payload,
        and Ethernet type (default is IPv4).
        """
        self.dest_mac = dest_mac
        self.src_mac = src_mac
        self.eth_type = eth_type
        self.payload = payload

    def pack(self):
        """
        Pack the Ethernet frame into bytes suitable for transmission.
        Ethernet header format is 6 bytes for Destination MAC, 6 bytes for Source MAC,
        and 2 bytes for Ethernet type. The payload follows the header.
        """
        header = struct.pack('!6s6sH', self.dest_mac, self.src_mac, self.eth_type)
        return header + self.payload

    @classmethod
    def unpack(cls, frame_bytes):
        """
        Unpack bytes into an EthernetFrame object.
        """
        dest_mac, src_mac, eth_type = struct.unpack('!6s6sH', frame_bytes[:14])
        payload = frame_bytes[14:]
        return cls(dest_mac, src_mac, payload, eth_type)

    @staticmethod
    def mac_str_to_bytes(mac_str):
        """
        Convert MAC address string (format XX:XX:XX:XX:XX:XX) to bytes.
        """
        return bytes.fromhex(mac_str.replace(':', ''))

    @staticmethod
    def mac_bytes_to_str(mac_bytes):
        """
        Convert MAC address bytes to string (format XX:XX:XX:XX:XX:XX).
        """
        return ':'.join(f'{b:02x}' for b in mac_bytes)

# Example usage
if __name__ == '__main__':
    src_mac = EthernetFrame.mac_str_to_bytes("00:0c:29:3d:5f:1d")
    dest_mac = EthernetFrame.mac_str_to_bytes("ff:ff:ff:ff:ff:ff")
    payload = b"Hello, Ethernet!"

    frame = EthernetFrame(dest_mac, src_mac, payload)
    frame_bytes = frame.pack()

    unpacked_frame = EthernetFrame.unpack(frame_bytes)
    print("Unpacked Frame:")
    print("Destination MAC:", EthernetFrame.mac_bytes_to_str(unpacked_frame.dest_mac))
    print("Source MAC:", EthernetFrame.mac_bytes_to_str(unpacked_frame.src_mac))
    print("Payload:", unpacked_frame.payload)
