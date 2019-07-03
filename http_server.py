#!/usr/local/bin/python3
# # -*- coding: UTF-8 -*-
import time
import os

while True:
    re = os.popen('netstat -tulnp').read()
    re_list = re.split('\n')
    re_list = re_list[2:-1]
    for a in re_list:
        if a.split()[3].split(':')[-1] == '80':
            print('HTTP (TCP/80) 服务已经被打开')
            break
    else:
         print('等待两秒重新开始监控!')
         time.sleep(2)
         continue
    break