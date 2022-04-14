# [문자열 생성] https://www.acmicpc.net/problem/6137

import sys
input = sys.stdin.readline
n = int(input())
s = t = ''
for _ in range(n):
    s += input().rstrip()
cnt = 0
lt, rt = 0, n-1
while lt <= rt:
    if s[lt] < s[rt]:
        t += s[lt]
        lt += 1
    elif s[lt] > s[rt]:
        t += s[rt]
        rt -= 1
    else:
        nl, nr = lt+1, rt-1
        while nl <= nr:
            if s[nl] < s[nr]:
                t += s[lt]
                lt += 1
                break
            elif s[nl] > s[nr]:
                t += s[rt]
                rt -= 1
                break
            else:
                nl += 1
                nr -= 1
        else:
            t += s[lt]
            lt += 1
    cnt += 1
    if cnt % 80 == 0:
        t += '\n'
print(t)
