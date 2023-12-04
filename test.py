import paho.mqtt.client as mqtt
import time

# Define the broker and topic
broker_address = "18.143.118.171"  # Replace with your MQTT broker's IP address
port = 1883  # Default MQTT port
topic = "test_topic"

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to the broker")
    else:
        print(f"Connection failed with code {rc}")

# Callback when a message is published
def on_publish(client, userdata, mid):
    print("Message published")

# Create an MQTT client
client = mqtt.Client()

# Set the callbacks
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the broker
client.connect(broker_address, port, keepalive=60)

# Loop to maintain the connection
client.loop_start()

# Publish a test message
message = "Hello, MQTT!"
result = client.publish(topic, message)

# Wait for the message to be sent (you can adjust this based on your needs)
time.sleep(2)

# Disconnect from the broker
client.loop_stop()
client.disconnect()
