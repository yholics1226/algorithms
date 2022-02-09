# [최고의 팀 만들기] https://www.acmicpc.net/problem/1633

import sys
arr = []
# for i in sys.stdin:
#     arr.append(list(map(int, i.split())))
while True:
    try:
        a, w = map(int, sys.stdin.readline().split())
        arr.append((a, w))
    except:
        break
n = len(arr)
dp = [[[0] * 16 for _ in range(16)] for _ in range(n+1)]
for i in range(n):
    for b in range(16):
        for w in range(16):
            if b < 15:
                dp[i+1][b+1][w] = max(dp[i+1][b+1][w], dp[i][b][w]+arr[i][0])
            if w < 15:
                dp[i+1][b][w+1] = max(dp[i+1][b][w+1], dp[i][b][w]+arr[i][1])
            dp[i+1][b][w] = max(dp[i+1][b][w], dp[i][b][w])
print(dp[n][15][15])
