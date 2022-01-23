# [팰린드롬 만들기] https://www.acmicpc.net/problem/1695

# using LCS (accepted in PyPy3, but time limit exceeded in Python3)
import sys
input = sys.stdin.readline
n = int(input())
nums = [*map(int, input().split())]
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if nums[-i] == nums[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(n - dp[n][n])

# another solution (memory exceeded..?)
import sys
input = sys.stdin.readline
n = int(input())
nums = [*map(int, input().split())]
dp = [[0] * n for _ in range(n)]
for i in range(1, n):
    for j in range(0, n-i):
        if nums[j] != nums[j+i]:
            dp[j][j+i] = min(dp[j][j+i-1], dp[j+1][j+i]) + 1
        else:
            dp[j][j+i] = dp[j+1][j+i-1]
print(dp[0][n-1])

# refactor (accepted in Python3 - 7192 ms, 30860 KB)
import sys
input = sys.stdin.readline
n = int(input())
arr = [*map(int, input().split())]
dp = [[0] * n for _ in range(3)]
for i in range(1, n):
    for j in range(n-i):
        dp[2][j] = dp[0][j+1] if arr[j] == arr[i+j] else 1 + min(dp[1][j], dp[1][j+1])
    dp[0], dp[1] = dp[1].copy(), dp[2].copy()
print(dp[1][0])
