import paho.mqtt.client as mqtt

mqtt_broker = "mosquitto"
mqtt_port = 1883
topics = ["tuya/data", "dht/data"]

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)

# Subscribe to multiple topics
for topic in topics:
    client.subscribe(topic)

client.on_message = on_message
client.loop_forever()
