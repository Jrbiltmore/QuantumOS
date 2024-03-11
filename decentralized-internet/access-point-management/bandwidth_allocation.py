class BandwidthAllocator:
    def __init__(self):
        self.devices = []
        self.total_bandwidth = 1000  # Total bandwidth in Mbps

    def add_device(self, device_id, priority):
        self.devices.append({"id": device_id, "priority": priority, "allocated_bandwidth": 0})
        self.allocate_bandwidth()

    def remove_device(self, device_id):
        self.devices = [device for device in self.devices if device["id"] != device_id]
        self.allocate_bandwidth()

    def allocate_bandwidth(self):
        # Simple allocation based on priority
        total_priority = sum(device["priority"] for device in self.devices)
        for device in self.devices:
            share = device["priority"] / total_priority
            device["allocated_bandwidth"] = round(self.total_bandwidth * share, 2)
        
        self.display_bandwidth_allocation()

    def display_bandwidth_allocation(self):
        for device in self.devices:
            print(f"Device {device['id']} allocated {device['allocated_bandwidth']} Mbps")

# Example usage
if __name__ == "__main__":
    allocator = BandwidthAllocator()
    allocator.add_device("Device1", priority=1)
    allocator.add_device("Device2", priority=2)
    allocator.add_device("Device3", priority=1)
    # Simulate removing a device
    allocator.remove_device("Device1")
