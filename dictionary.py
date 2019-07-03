# 字典课堂作业
import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n \
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}

for conn in asa_conn.split('\n'):
    re_result = re.match('.+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):('
    '\d{1,5}).+bytes\s+(\d+).+flags\s+(\w*)\s*', conn).groups()

    key           = re_result[0], re_result[1], re_result[2], re_result[3]
    value         = re_result[4], re_result[5]
    asa_dict[key] = value

print('打印分析后的字典！\n')
print(asa_dict)

src         = 'src'
src_ip      = 'src_ip'
dst         = 'dst'
dst_ip      = 'dst_ip'
bytes_name  = 'bytes'
flags       = 'flags'

print('\n格式化打印输出\n')

for key, value in asa_dict.items():
    print('%10s : %-15s |%10s : %-10s |%6s : %-10s|%10s : %-10s' % (src, key[0], src_ip, key[1], dst, key[2], dst_ip, key[3]))
    print('%10s : %-15s |%10s : %-10s' % (bytes_name, value[0], flags, value[1]))
    print('=' * 110)
