import Adafruit_DHT
import paho.mqtt.client as mqtt
from pymongo import MongoClient
from time import sleep
import json
import requests

# DHT Sensor configuration
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO pin where the sensor is connected

# MQTT configuration
MQTT_BROKER = "localhost"  # Use the IP address of your MQTT broker
MQTT_PORT = 1883
MQTT_TOPIC = "dht/data"

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27020/"  # Adjust the port if needed
MONGO_DB = "dht22_logs"
MONGO_COLLECTION = "log_dht"

# Telegram Bot configuration
BOT_TOKEN = "7753236581:AAGSmgbgZb7KSStvCscKMwAX5q0IdSsBu3c"
CHAT_ID = "6820132381"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Initialize MongoDB client
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Initialize MQTT client
mqtt_client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")

def send_telegram_notification(message):
    try:
        response = requests.post(TELEGRAM_URL, data={'chat_id': CHAT_ID, 'text': message})
        if response.status_code == 200:
            print("Notification sent to Telegram")
        else:
            print("Failed to send notification to Telegram")
    except Exception as e:
        print(f"Error sending Telegram notification: {e}")

def publish_dht_data():
    try:
        # Read temperature and humidity from DHT22 sensor
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        
        if humidity is not None and temperature is not None:
            # Create data payload
            data = {
                "temperature": temperature,
                "humidity": humidity,
                "timestamp": sleep.time()
            }
            
            # Publish data to MQTT topic
            mqtt_client.publish(MQTT_TOPIC, json.dumps(data))
            print(f"Published to MQTT topic {MQTT_TOPIC}: {data}")

            # Save data to MongoDB
            collection.insert_one(data)
            print("Data saved to MongoDB")
            
            # Check if temperature or humidity exceeds the threshold
            if temperature >= 40 or humidity >= 80:
                message = f"Alert! Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%"
                send_telegram_notification(message)
        else:
            print("Failed to retrieve data from the sensor.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Connect to MQTT broker
    mqtt_client.on_connect = on_connect
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()
    
    # Continuous data reading and publishing
    while True:
        publish_dht_data()
        sleep(5)  # Wait 5 seconds before reading again
