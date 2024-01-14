import csv,time
import paho.mqtt.client as mqtt

# Define the broker and topic
broker_address = "192.168.60.154"  # Replace with your MQTT broker's IP address
port = 1883  # Default MQTT port

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

with open('../resource/debs40houses16h/house-0.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            payload = ','.join(line) # Join the CSV elements into a string
            print(line)  
            print(payload)
            client.publish("test_topic", payload)
            time.sleep(0.1)


# Loop to maintain the connection
client.loop_start()
