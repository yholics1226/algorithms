# [Delete Operation for Two Strings] https://leetcode.com/problems/delete-operation-for-two-strings/

def minDistance(word1, word2):
    n, m = len(word1), len(word2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if word1[i] == word2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return n + m - 2 * dp[n][m]

# faster solution
import bisect
def minDistance(word1, word2):
    n, m = len(word1), len(word2)
    dp = []
    for c in word1:
        for i in range(m-1, -1, -1):
            if c == word2[i]:
                idx = bisect.bisect_left(dp, i)
                if idx == len(dp):
                    dp.append(i)
                else:
                    dp[idx] = i
    return n + m - 2 * len(dp)
