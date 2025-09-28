import paho.mqtt.client as mqtt
import json
import time

# MQTT broker details
BROKER_IP = "192.168.1.50"
BROKER_PORT = 1883  # default MQTT port
TOPIC = "sensor/data"

# Payload to send
payload = {
    "tem": 26,
    "hum": 61,
    "st": "st-1",
    "st_id": "uifuf"
}

# Callback for connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to EMQX broker")
        # client.publish(TOPIC, json.dumps(payload), qos=1)
        client.publish(TOPIC, json.dumps(payload), qos=1, retain=True)
        print(f"📤 Published to topic '{TOPIC}': {payload}")
    else:
        print(f"❌ Connection failed with code {rc}")

# Create MQTT client
client = mqtt.Client()

# Assign callback
client.on_connect = on_connect

# Connect to broker
client.connect(BROKER_IP, BROKER_PORT, keepalive=60)

# Start loop to process network traffic and callbacks
client.loop_start()

# Give it time to publish before exiting
time.sleep(2)
client.loop_stop()
client.disconnect()
