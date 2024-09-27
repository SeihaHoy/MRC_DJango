import paho.mqtt.client as mqtt
from random import randrange,uniform,random
import math
import time

mqttBroker = "broker.emqx.io" #Our mosquitto broker running on 127.0.0.1
client = mqtt.Client() #instantiating the mqtt client.

client.connect(mqttBroker,port=1883) #Connecting mqtt client to broker.
i=0
#The loop just sends random sin values to a topic in broker.
while i < 2000:
    num = math.sin(i) #Sine value of i
    #id = randrange(1,5)
    id=randrange(4,8) #Id of our sensor in backend.
    client.publish(f"SENSOR/{id}",num) #Publish the number to topic 'Sensor/id_of_sensor'
    print(f"Just published {num} to topic SENSOR/{id} with count {i}")
    i = i+1
    time.sleep(0.5)

