# [괄호] https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    ps = input().rstrip()
    cnt = 0
    for p in ps:
        if p == '(':
            cnt += 1
        elif cnt:
            cnt -= 1
        else:
            print('NO')
            break
    else:
        print('NO' if cnt else 'YES')
