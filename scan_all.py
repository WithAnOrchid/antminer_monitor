# coding: utf-8
import discover
import scan

d = discover.Discover()

miner_list = d.discoverNetwork()
print(u'找到{0}台矿机'.format(len(miner_list)))
# maintain_mode=True 会让程序在扫描到新矿机时，打印一条额外的提示
# 通过查看矿工名是否是蚂蚁默认值来决定
s = scan.Scan(miner_list=miner_list, maintain_mode=True)
results = s.readAllStats()
print(u'获取到{0}个矿机信息'.format(len(results)))

print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

# 注意 矿机信息列表里面存的是tuple
# 此tuple的格式是['ip','mac','worker','time','stats']
for result in results:
    print('----------------------------------------------')
    print(result.ip+ " " + result.worker)
    #if result.ip == "192.168.101.100":
       # print(result.stats)
