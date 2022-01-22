# [생태학] https://www.acmicpc.net/problem/4358

import sys
input = sys.stdin.readline
nlist = []
ndict = dict()
n = 0
while True:
    x = input().strip()
    if not x:
        break
    if x in ndict:
        ndict[x] += 1
    else:
        ndict[x] = 1
        nlist.append(x)
    n += 1
nlist.sort()
for x in nlist:
    print(x, '%.4f' % (ndict[x] / n * 100))
