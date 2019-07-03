# 正则表达式练习：查看linux网关
import os
import re
import codecs
import sys

# 中文输出
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# 查找并输出网关
route_n_result = os.popen('route -n').read()
ipv4_gw = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+UG', route_n_result)[0]
print('网关为:' + str(ipv4_gw))
