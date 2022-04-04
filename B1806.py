# [부분합] https://www.acmicpc.net/problem/1806

import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = [*map(int, input().split())]
if sum(arr) < s:
    print(0)
else:
    ans = n
    lt, rt = 0, 1
    ps = arr[lt]
    while lt < n:
        if ps < s:
            if rt < n:
                ps += arr[rt]
                rt += 1
            else:
                break
        else:
            ans = min(ans, rt - lt)
            ps -= arr[lt]
            lt += 1
    if ps >= s:
        ans = min(ans, rt - lt)
    print(ans)
    
# refactor
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = [*map(int, input().split())]
if sum(arr) < s:
    print(0)
else:
    ans = n
    ps = lt = rt = 0
    while True:
        if ps >= s:
            ans = min(ans, rt - lt)
            ps -= arr[lt]
            lt += 1
        elif rt == n:
            break
        else:
            ps += arr[rt]
            rt += 1
    print(ans)
