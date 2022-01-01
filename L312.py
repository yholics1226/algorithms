# [Burst Balloons] https://leetcode.com/problems/burst-balloons/

def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for i in range(1, n-1):
        for lt in range(1, n-i):
            rt = lt + i - 1
            for j in range(lt, rt+1):
                dp[lt][rt] = max(dp[lt][rt], dp[lt][j-1] + nums[lt-1] * nums[j] * nums[rt+1] + dp[j+1][rt])
    return dp[1][-2]
