import paho.mqtt.client as mqtt
import requests
import sys
import time
import json


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    topic = "connect"

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    """
    The on_message callback takes 3 arguments:
    1 : client
    2 : userdata
    3 : msg

    The data sent from broker is stored in the 'msg' argument.
    It contains both the 'topic' the data was received from,
    and the payload.

    We parse the topic to get the id of the sensor.
    And we get the payload from msg.payload as well.

    We then send this data to our API.

    You can create a database connection in this file, and instead
    store the data directly in the database, that would be
    preferred in production environments.
    """
    print(msg.topic + " " + str(msg.payload))
    # url = "http://localhost:8000/sensors/readings/"

    # Parse the JSON payload
    payload = json.loads(msg.payload)

    # Extract device_id, water_level, and rain_fall from the payload
    device_id = payload.get("device_id")
    water_level = payload.get("water_level")
    rain_fall = payload.get("rain_fall")
    print(device_id)

    data = {"device_id": device_id, "water_level": water_level, "rain_fall": rain_fall}
    # requests.post(url, data)


# Connection to the client is established here
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.emqx.io", port=1883)
client.loop_forever()
