# [Decode Ways] https://leetcode.com/problems/decode-ways/

def numDecodings(s):
    if s[0] == '0':
        return 0
    else:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(1, n):
            if s[i] == '0':
                if s[i-1] != '1' and s[i-1] != '2':
                    return 0
                else:
                    dp[i+1] = dp[i-1]
            elif s[i-1] == '0':
                dp[i+1] = dp[i]
            elif int(s[i-1:i+1]) <= 26:
                dp[i+1] = dp[i-1] + dp[i]
            else:
                dp[i+1] = dp[i]
        return dp[-1]

# simplified version
def numDecodings(s):
    if s[0] == '0':
        return 0
    else:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(1, n):
            if s[i] != '0':
                dp[i+1] += dp[i]
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
        return dp[-1]

# another solution using DFS (much slower than the methods above..)
def numDecodings(s):
    dy = [0] * 120
    def DFS(L):
        if s[0] == '0':
            return 0
        if dy[L] > 0:
            return dy[L]
        if L < len(s) and s[L] == '0':
            return 0
        if L == len(s)-1 or L == len(s):
            return 1
        answer = DFS(L+1)
        tmp = int(s[L:L+2])
        if tmp <= 26:
            answer += DFS(L+2)
        dy[L] = answer
        return dy[L]
    return DFS(0)
