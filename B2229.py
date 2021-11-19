# [조 짜기] https://www.acmicpc.net/problem/2229

n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n
for i in range(1, n):
    dp[i] = max(nums[:i+1]) - min(nums[:i+1])
    for j in range(i):
        dp[i] = max(dp[i], dp[j] + max(nums[j+1:i+1]) - min(nums[j+1:i+1]))
print(dp[-1])

# refactor
n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n
for i in range(1, n):
    dp[i] = max(nums[:i+1]) - min(nums[:i+1])
    maxn, minn = 0, 10000
    for j in range(i, 0, -1):
        maxn, minn = max(maxn, nums[j]), min(minn, nums[j])
        dp[i] = max(dp[i], dp[j-1] + maxn - minn)
print(dp[-1])
