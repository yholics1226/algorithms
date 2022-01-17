# [달리기] https://www.acmicpc.net/problem/2517

import sys
input = sys.stdin.readline
n = int(input())
nums = [(i, int(input())) for i in range(n)]
nums.sort(key=lambda x: x[1], reverse=True)
m = 1
while m < n:
    m *= 2
tree = [0] * (m * 2)
ans = [0] * n
def update(idx):
    while idx > 0:
        tree[idx] += 1
        idx = idx // 2
def get(s, idx):
    rank = 0
    while s <= idx:
        if s % 2 == 1:
            rank += tree[s]
        if idx % 2 == 0:
            rank += tree[idx]
        s = (s + 1) // 2
        idx = (idx - 1) // 2
    return rank
for idx, _ in nums:
    update(m + idx)
    ans[idx] = get(m, m + idx)
for x in ans:
    print(x)
