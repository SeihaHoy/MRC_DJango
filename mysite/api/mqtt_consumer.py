import paho.mqtt.client as mqtt
import json, logging
from .models import Sensors, SensorData  # Import your Django models
from django.conf import settings

BROKER_URL= settings.MQTT_BROKER_HOST
TOPIC = settings.MQTT_CENTRAL_TOPIC

def on_connect(client, userdata, flags, rc):
    logging.info("Connected to MQTT broker with result code " + str(rc))
    client.subscribe(TOPIC)
    logging.info(f"Django is connected to the topic {TOPIC}")
    # Subscribe to MQTT topics, if needed


def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode("utf-8"))
    device_id = payload['device_id']
    message_type = payload['message_type']
    if message_type == 'registration':
        # Create a new device
        try:#
            Sensors_available  = Sensors.objects.filter(device_id=device_id).exists()
            if Sensors_available:
                Sensors = Sensors.objects.get(device_id=device_id)
                logging.warning("Sensors is already available")
            else:
                logging.warning("Sensors is not available")
                Sensors = Sensors(device_id=device_id)
                Sensors.save()
        except Sensors.DoesNotExist:
            logging.error("Sensors doesn't exist")

    elif message_type == 'update':
        # Find the Sensors and create a measurement
        Sensors_available  = Sensors.objects.filter(device_id=device_id).exists()
        if Sensors_available:
            Sensors = Sensors.objects.get(device_id=device_id)
            measurement = SensorData(Sensors=Sensors,water_level=payload['water_level'], rain_fall=payload['rain_fall'])
            # print(device_id, message_type, payload)
            measurement.save()
        else:
            logging.warning("Sensors is not available")

    elif message_type == 'deregistration':
        # Delete the Sensors and its measurements
        Sensors_available  = Sensors.objects.filter(device_id=device_id).exists()
        if Sensors_available:
            Sensors.objects.filter(device_id=device_id).delete()
    else:
        logging.warning(f"Unknown message type is sent, message:{payload}")


    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_URL, 1883, 60)