# [222-풀링] https://www.acmicpc.net/problem/17829

import sys
input = sys.stdin.readline
n = int(input())
nums = [[*map(int, input().split())] for _ in range(n)]
while n > 1:
    n //= 2
    nxt = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = [nums[i*2][j*2], nums[i*2][j*2+1], nums[i*2+1][j*2], nums[i*2+1][j*2+1]]
            tmp.sort()
            nxt[i][j] = tmp[-2]
    nums = nxt.copy()
print(nums[0][0])
