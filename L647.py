# [Palindromic Substrings] https://leetcode.com/problems/palindromic-substrings/

def countSubstrings(s):
    n = len(s)
    cnt = n
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            cnt += 1
    for i in range(2, n):
        for j in range(n-i):
            if s[j] == s[j+i] and dp[j+1][j+i-1]:
                dp[j][j+i] = True
                cnt += 1
    return cnt
