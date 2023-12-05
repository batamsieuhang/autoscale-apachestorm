import csv
import time
import paho.mqtt.client as mqtt

# Define the broker and topic
broker_address = "192.168.60.154"  # Replace with your MQTT broker's IP address
port = 1883  # Default MQTT port
topic = "test_topic"  # The topic you want to subscribe to

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to the broker")
        client.subscribe(topic)  # Subscribe to the desired topic
    else:
        print(f"Connection failed with code {rc}")


# Callback when a message is received
def on_message(client, userdata, msg):
    payload_decoded = msg.payload.decode()
    print(f"Received message on topic {msg.topic}: {payload_decoded}")

# Create an MQTT client
client = mqtt.Client()

# Set the callbacks
client.on_connect = on_connect

client.on_message = on_message  # Add the on_message callback

# Connect to the broker
client.connect(broker_address, port, keepalive=60)

# Loop to maintain the connection
client.loop_start()

while True:
    time.sleep(1)