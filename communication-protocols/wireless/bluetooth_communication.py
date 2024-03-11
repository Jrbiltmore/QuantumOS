import bluetooth

def discover_devices():
    print("Discovering nearby Bluetooth devices...")
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    for addr, name in nearby_devices:
        print(f"Found Bluetooth device {name} with address {addr}")

def make_device_discoverable(duration=60):
    print("Making device discoverable...")
    mode = bluetooth.get_discoverable()
    bluetooth.set_discoverable(duration)
    return mode

def start_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = bluetooth.PORT_ANY
    server_sock.bind(("", port))
    server_sock.listen(1)
    bluetooth.advertise_service(server_sock, "SampleServer", service_id=bluetooth.SERIAL_PORT_CLASS)
    
    print("Waiting for connection on RFCOMM channel", port)
    client_sock, client_info = server_sock.accept()
    print("Accepted connection from", client_info)
    
    try:
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            print("Received:", data.decode('utf-8'))
            client_sock.send("Echo => " + data.decode('utf-8'))
    except IOError:
        pass
    
    print("Disconnected.")
    client_sock.close()
    server_sock.close()

def start_client(server_address):
    port = 1  # Use the same port number as the server.
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((server_address, port))
    print("Connected to", server_address)
    
    message = "Hello, Bluetooth!"
    sock.send(message)
    print("Sent:", message)
    response = sock.recv(1024)
    print("Received:", response.decode('utf-8'))
    
    sock.close()

# Example usage
if __name__ == '__main__':
    discover_devices()
    # Uncomment these lines to run the server or client parts.
    # Make sure to use the correct Bluetooth address for the client function.
    #start_server()
    #start_client('XX:XX:XX:XX:XX:XX')  # Replace with server's Bluetooth address.
