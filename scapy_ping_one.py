#!/usr/local/bin/python3
# # -*- coding: UTF-8 -*-
import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *


def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False) # 获取响应信息，超时为2秒，关闭详细信息
    if ping_result:
        return ip, 1
    else:
        return ip, 0

if __name__ == '__main__':
    result = qytang_ping('192.168.2.1')
    if result[1]:
        print(result[0], '通!')
    else:
        print(result[0], '不通!')