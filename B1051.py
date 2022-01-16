# [숫자 정사각형] https://www.acmicpc.net/problem/1051

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = [input() for _ in range(n)]
for k in range(min(n, m)-1, 0, -1):
    for i in range(n-k):
        for j in range(m-k):
            if nums[i][j] == nums[i+k][j] == nums[i][j+k] == nums[i+k][j+k]:
                print((k+1)**2)
                sys.exit(0)
print(1)
