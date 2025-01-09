import paho.mqtt.client as mqtt

mqtt_broker = "mosquitto"
mqtt_port = 1883
topic = "sensor/data"

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)
client.publish(topic, "tuya data message") #tuya data
client.disconnect()
