import ssl
import time
import os
import paho.mqtt.client as mqtt

# — MQTT Config —
endpoint = 'asfsaffsafasf-ats.iot.ap-southeast-1.amazonaws.com'
port = 8883
topic = "mytest/1234"
message = "Hello from Python MQTT"

# Absolute paths to your certs
ca_path   = r"C:/Users/cloud-wintun/Desktop/iot-core-cert-1/st-1-esp32-ca1.pem"
cert_path = r"C:/Users/cloud-wintun/Desktop/iot-core-cert-1/st-1-esp32-certificate.pem.crt"
key_path  = r"C:/Users/cloud-wintun/Desktop/iot-core-cert-1/st-1-esp32-private.pem.key"

# Sanity check
for path in [ca_path, cert_path, key_path]:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Missing file: {path}")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"📥 Received: {msg.topic} → {msg.payload.decode()}")

# Callback when connected
def on_connect(client, userdata, flags, rc):
    print(f"🔌 Connected with result code {rc}")
    client.subscribe(topic)
    print(f"📡 Subscribed to topic: {topic}")
    client.publish(topic, message)
    print(f"📤 Published message: {message}")

# # Create client
# client = mqtt.Client(protocol=mqtt.MQTTv311)

# # Configure TLS
# client.tls_set(ca_certs=ca_path,
#                certfile=cert_path,
#                keyfile=key_path,
#                tls_version=ssl.PROTOCOL_TLSv1_2)

client = mqtt.Client(protocol=mqtt.MQTTv311)
print("ujfaf",client)
client.tls_set(ca_certs=ca_path, certfile=cert_path, keyfile=key_path, tls_version=ssl.PROTOCOL_TLSv1_2)

# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect and loop
client.connect(endpoint, port)
client.loop_start()

# Keep alive for 10 seconds to receive messages
time.sleep(10)

# Clean up
client.loop_stop()
client.disconnect()
print("✅ MQTT session complete.")
