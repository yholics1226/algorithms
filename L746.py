# [Min Cost Climbing Stairs] https://leetcode.com/problems/min-cost-climbing-stairs/

def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * n
    dp[-1], dp[-2] = cost[-1], cost[-2]
    for i in range(n-3, -1, -1):
        dp[i] = cost[i] + min(dp[i+1], dp[i+2])
    return min(dp[0], dp[1])

# another solution
def minCostClimbingStairs(cost):
    c1, c2 = cost[0], cost[1]
    for i in range(2, len(cost)):
        c1, c2 = c2, min(c1, c2) + cost[i]
    return min(c1, c2)
