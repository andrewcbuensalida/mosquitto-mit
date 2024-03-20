import paho.mqtt.client as mqtt
import json
import time
import random

topic = "sensors/temperatures"
broker = "localhost"
port = 1883

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION1
)  # had to add mqtt.CallbackAPIVersion.VERSION1 so it would work. (based on https://github.com/eclipse/paho.mqtt.python/blob/v2.0.0/docs/migrations.rst). without this it would error TypeError: Client.__init__() missing 1 required positional argument: 'callback_api_version'
client.connect(broker, port, 60)
print(f"connected on {port}")

for i in range(100):
    data = json.dumps({"temperature": random.randint(0, 100)}) # dumps stringifies object
    client.publish(topic, data)
    print(f"published: {data}")
    time.sleep(1)

client.disconnect
