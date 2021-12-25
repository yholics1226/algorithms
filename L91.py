# [Decode Ways] https://leetcode.com/problems/decode-ways/

def numDecodings(s):
    dp = [0] * 120

    def DFS(L):
        if s[0] == '0':
            return 0
        if dp[L] > 0:
            return dp[L]
        if L < len(s) and s[L] == '0':
            return 0
        if L == len(s)-1 or L == len(s):
            return 1

        answer = DFS(L+1)
        tmp = int(s[L:L+2])
        if tmp <= 26:
            answer += DFS(L+2)
        dp[L] = answer
        return dp[L]

    return DFS(0)
