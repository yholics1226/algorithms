# [Champagne Tower] https://leetcode.com/problems/champagne-tower/

def champagneTower(poured, query_row, query_glass):
    dp = [[0] * i for i in range(1, 101)]
    dp[0][0] = poured
    for i in range(query_row):
        for j in range(i+1):
            excess = (dp[i][j] - 1) / 2
            if excess > 0:
                dp[i+1][j] += excess
                dp[i+1][j+1] += excess
    return min(1, dp[query_row][query_glass])
