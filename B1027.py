# [고층 건물] https://www.acmicpc.net/problem/1027

import sys
input = sys.stdin.readline
n = int(input())
arr = [*map(int, input().split())]
num = [0] * n
for i in range(n):
    s = float('-inf')
    for j in range(i+1, n):
        slope = (arr[j] - arr[i]) / (j - i)
        if slope > s:
            s = slope
            num[i] += 1
            num[j] += 1
print(max(num))
