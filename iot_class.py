from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import json
from config import farmLocation, iotConfig
import ssh_reboot

clientId = farmLocation
host = iotConfig['host']
caPath = iotConfig['caPath']
certPath = iotConfig['certPath']
keyPath = iotConfig['keyPath']


class IOT:
    def __init__(self):
        # Init AWSIoTMQTTClient
        self.device = AWSIoTMQTTClient(clientId)
        self.device.configureEndpoint(host, 8883)
        self.device.configureCredentials(caPath, keyPath, certPath)

        # AWSIoTMQTTClient connection configuration
        self.device.configureAutoReconnectBackoffTime(1, 32, 20)
        self.device.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.device.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.device.configureConnectDisconnectTimeout(10)  # 10 sec
        self.device.configureMQTTOperationTimeout(5)  # 5 sec

    # Custom MQTT message callback
    def customCallback(self, client, userdata, message):
        print("AWS IoT message received. Topic={}, Payload={}"
              .format(message.topic, message.payload))
        print("--------------\n\n")
        # if message.topic == 'rebootCommandguyi':
        #     # execute the reboot function
        #     info = json.loads(message.payload)
        #     location = info['Location']
        #     ip = info['ID']
        #     ssh_reboot.sshAndReboot(ip, location).judgements()

    def conn(self):
        # Connect and subscribe to AWS IoT
        try:
            print('AWS IoT connecting...')
            self.device.connect(1200)
            print('AWS IoT connected')
            self.device.subscribe(iotConfig['controlSubscribeTo'], 1, self.customCallback)
            self.device.subscribe("rebootCommandguyi", 1, self.customCallback)
            self.device.subscribe("controlsignal", 1, self.customCallback)
            # publish to AWS IoT
            status = {
                "status": 'connected'
            }
            self.device.publish(iotConfig['controlPublishTo'], json.dumps(status), 1)
            time.sleep(1)

        except:
            print('AWS IoT not connected.')

    def publish_miner_details(self, information):
        self.device.publish(iotConfig['minerDetailsPublishTo'] + '', information, 1)

    def publish_scheduled_miner_details(self, information):
        self.device.publish(iotConfig['scheduledPublishTo'] + '', information, 1)

    def publish_general_info(self, information):
        self.device.publish(iotConfig['generalInfoPublishTo'] + '', information, 1)

    def publish_to(self, topic, information):
        farm_location = farmLocation + '/' + topic
        self.device.publish(farm_location, information, 1)


