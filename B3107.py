# [IPv6] https://www.acmicpc.net/problem/3107

import sys
ip = sys.stdin.readline().strip().split(':')
if len(ip) > 8:
    if ip[0] == '' and ip[1] == '':
        ip = ip[1:]
    else:
        ip.pop()
if ip[0] == '':
    ip[0] = '0000'
if ip[-1] == '':
    ip[-1] = '0000'
flag = 1 if len(ip) != 8 else 0
for i in range(len(ip)):
    l = len(ip[i])
    if flag and l == 0:
        ip[i] = '0000' + ':0000' * (8-len(ip))
    elif l < 4:
        ip[i] = '0' * (4 - l) + ip[i]
print(':'.join(ip))
