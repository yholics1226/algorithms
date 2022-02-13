# [싸이버개강총회] https://www.acmicpc.net/problem/19583

import sys
input = sys.stdin.readline
s, e, q = input().split()
attend = set()
flag = False
cnt = 0
while True:
    try:
        t, n = input().split()
        if flag:
            continue
        if t <= s:
            attend.add(n)
        elif t >= e:
            if t <= q:
                if n in attend:
                    cnt += 1
                    attend.remove(n)
            else:
                flag = True
    except:
        break
print(cnt)
