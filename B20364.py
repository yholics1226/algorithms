# [부동산 다툼] https://www.acmicpc.net/problem/20364

import sys
input = sys.stdin.readline
n, q = map(int, input().split())
tree = [0] * (n+1)
for _ in range(q):
    x = int(input())
    ans = x if tree[x] else 0
    tree[x] = 1
    while x > 1:
        x >>= 1
        if tree[x]:
            ans = x
    print(ans)
