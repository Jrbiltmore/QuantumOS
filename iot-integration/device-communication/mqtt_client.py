import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("your/topic")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

def on_publish(client, userdata, mid):
    print(f"Message published with mid {mid}")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish

    # Connect to an MQTT broker
    client.connect("mqtt.eclipseprojects.io", 1883, 60)

    # Publishing a message to a topic
    client.publish("your/topic", "Hello MQTT!")

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()

if __name__ == "__main__":
    main()
