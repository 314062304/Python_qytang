# 课后作业(2)
import re
str1 = 'Port-channel1.189          192.168.168.254    yes    config    up '

result = re.match('\s*(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)\s+(\w*)\s*', str1).groups()

print(result)
print('-'*80)
print('%-6s : %s' % ('接口', result[0]))
print('%-6s : %s' % ('IP地址', result[1]))
print('%-6s : %s' % ('方法', result[3]))
print('%-6s : %s' % ('状态',  result[4]))





