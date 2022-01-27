# [Contact] https://www.acmicpc.net/problem/1013

import re, sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = input().strip()
    p = re.compile('(100+1+|01)+')
    print('YES') if p.fullmatch(s) else print('NO')
