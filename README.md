### MQTT
- MQTT operates over TCP/IP, and optionally over TLS for secure transport. 
- Application layer protocol, meaning it defines how messages are structured and exchanged — not how they’re physically transmitted.

### Popular MQTT Brokers for Local Testing

- Mosquitto (by Eclipse): Lightweight, widely used, perfect for local setups.
- EMQX: More feature-rich, supports clustering, authentication, and dashboards.
- HiveMQ CE: Community edition with a web UI and plugin support.
- VerneMQ: Scalable and written in Erlang, great for high-throughput setups.

### Default MQTT Ports

Port	Protocol	Description
1883	TCP	Standard MQTT (unencrypted)
8883	TCP	MQTT over TLS/SSL (secure)
8080	HTTP	MQTT over WebSockets (optional)
9001	WebSocket	MQTT over WebSockets (used by Mosquitto and others)

#### Usage
- 1883 for local testing or internal networks.
- 8883 when security matters — e.g., cloud brokers like AWS IoT Core.
- 9001 if you're integrating MQTT with browser-based clients or dashboards.