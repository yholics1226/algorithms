# [Delete and Earn] https://leetcode.com/problems/delete-and-earn/

def deleteAndEarn(nums):
    pts = [0] * (max(nums) + 1)
    for num in nums:
        pts[num]+= num
    n = len(pts)
    if n <= 2:
        return max(pts)
    dp = [0] * n
    dp[0] = pts[0]
    dp[1] = max(pts[0], pts[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + pts[i])
    return dp[-1]

# another solution
from collections import Counter
def deleteAndEarn(nums):
    cnt = Counter(nums)
    prev = cur = 0
    for i in range(max(nums)+1):
        prev, cur = cur, max(cur, prev + i * cnt[i])
    return cur
