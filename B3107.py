# [IPv6] https://www.acmicpc.net/problem/3107

import sys
ip = sys.stdin.readline().strip().split(':')
if ip[0] == '':
    ip[0] = '0000'
if ip[-1] == '':
    ip[-1] = '0000'
flag = 1 if len(ip) != 8 else 0
for i in range(len(ip)):
    if flag and len(ip[i]) == 0:
        ip[i] = '0000' + ':0000' * (8-len(ip))
    elif len(ip[i]) < 4:
        ip[i] = '0' * (4 - len(ip[i])) + ip[i]
print(':'.join(ip))
