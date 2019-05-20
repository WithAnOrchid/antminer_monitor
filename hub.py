import discover
import scan
import logging
from config import farmLocation, iotConfig
import iot_class
import json

logger = logging.getLogger()  # initialize logging class
logger.setLevel(logging.ERROR)


class Hub:
    def __init__(self, caller):
        self.caller = caller

    def discoverRound(self):
        logger.info('***Starting Scanning Round***')
        #  获取所有矿机的IP和MAC地址
        miner_list = discover.Discover().discoverNetwork()  # [(ip, mac)]
        #  获取矿机运行数据
        s = scan.Scan(miner_list=miner_list, maintain_mode=True)
        results = s.readAllStats()
        device = iot_class.IOT()
        device.conn()
        for result in results:
            reslist = result.stats
            reslist['general'] = {
                    "location": farmLocation,
                    "ip": result.ip,
                    "mac": result.mac,
                    "worker": result.worker,
                    "timestamp": result.time
                }
            if self.caller == 'scheduler':
                device.publish_scheduled_miner_details(json.dumps(reslist))
                # # iot.publish_scheduled_miner_details(json.dumps(reslist))
                # device.publish(iotConfig['scheduledPublishTo'] + '', json.dumps(reslist), 1)









