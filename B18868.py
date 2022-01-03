# [멀티버스 1] https://www.acmicpc.net/problem/18868

import sys
input = sys.stdin.readline
m, n = map(int, input().split())
U = [list(map(int, input().split())) for _ in range(m)]
def sim(a, b):
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] < a[j] and b[i] >= b[j]:
                return 0
            elif a[i] == a[j] and b[i] != b[j]:
                return 0
            elif a[i] > a[j] and b[i] <= b[j]:
                return 0
    return 1
cnt = 0
for i in range(m-1):
    for j in range(i+1, m):
        cnt += sim(U[i], U[j])
print(cnt)

# another solution (faster)
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
U = [list(map(int, input().split())) for _ in range(m)]
cnt = 0
for i in range(m):
    sU = sorted(U[i])
    idx = []
    for p in U[i]:
        idx.append(sU.index(p))
    U[i] = idx
for i in range(m-1):
    for j in range(i+1, m):
        if U[i] == U[j]:
            cnt += 1
print(cnt)
