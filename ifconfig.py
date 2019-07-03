# 正则表达式测试练习
import os
import re

ifconfig_result = 'ens160: flags=4163<UP, BROADCAST, RUNNING, MULTICAST> mtu 1500\n  inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255\n  inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>\n    ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)\n      RX packets 174598769 bytes 1795658527217 (1.6 TiB)\n         RX errors 1 dropped 24662 overruns 0 frame 0\n      TX packets 51706604 bytes 41788673420 (38.9 GiB)\n      TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0\n\n'

# 正则表达式查找ip，掩码，广播和MAC地址
ipv4_add    =   re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
netmask     =   re.findall('([0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{1,3})', ifconfig_result)[0]
broadcast   =   re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.[2-5]{1,3})', ifconfig_result)[0]
mac_addr    =   re.findall('([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})', ifconfig_result)[0]



# 格式化字符串
format_string = '%-10s : %s' % ('ipv4_add', ipv4_add), '%-10s : %s' % ('netmask', netmask), '%-10s : %s' % ('broadcast', broadcast), '%-10s : %s' % ('mac_addr', mac_addr)

# 打印结果
print(format(format_string[0]))
print(format(format_string[1]))
print(format(format_string[2]))
print(format(format_string[3]))


# 产生网关的IP地址
ipv4_gw = '172.16.66.254'

# 打印网关的IP地址
print('\n我们假设网关IP地址为最后一位为254， 因此网关IP地址为：' + ipv4_gw + '\n')

# ping网关
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()

re_ping_result = re.match('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ping_result)

if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')