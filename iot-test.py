
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import json
from config import farmLocation, iotConfig


clientId = farmLocation
host = iotConfig['host']
caPath = iotConfig['caPath']
certPath = iotConfig['certPath']
keyPath = iotConfig['keyPath']


# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("AWS IoT message received. Topic={}, Payload={}"
          .format(message.topic, message.payload))
    print("--------------\n\n")


def offline():
    print('aws iot is offline.')


# Init AWSIoTMQTTClient
device = AWSIoTMQTTClient(clientId)
device.configureEndpoint(host, 8883)
device.configureCredentials(caPath, keyPath, certPath)


# AWSIoTMQTTClient connection configuration
device.configureAutoReconnectBackoffTime(1, 32, 20)
device.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
device.configureDrainingFrequency(2)  # Draining: 2 Hz
device.configureConnectDisconnectTimeout(10)  # 10 sec
device.configureMQTTOperationTimeout(5)  # 5 sec
device.onOffline = offline


# Connect and subscribe to AWS IoT
try:
    print('AWS IoT connecting...')
    device.connect(1200)
    print('AWS IoT connected')
    while True:
        device.subscribe(iotConfig['controlSubscribeTo'], 1, customCallback)
        device.subscribe("rebootCommandguyi", 1, customCallback)
        device.subscribe("controlsignal", 1, customCallback)
        # publish to AWS IoT
        status = {
            "status": 'connected'
        }
        device.publish(iotConfig['controlPublishTo'], json.dumps(status), 1)
        time.sleep(1)
except:
    print('AWS IoT not connected.')



