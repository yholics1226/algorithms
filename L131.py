# [Palindrome Partitioning] https://leetcode.com/problems/palindrome-partitioning/

def partition(s):
    def isPalindrome(lt, rt):
        while lt < rt:
            if s[lt] != s[rt]:
                return False
            lt += 1
            rt -= 1
        return True
    n = len(s)
    dp = [[] for _ in range(n+1)]
    dp[0].append([])
    for i in range(n):
        for j in range(i+1):
            if isPalindrome(j, i):
                sub = s[j:i+1]
                for lst in dp[j]:
                    dp[i+1].append(lst + [sub])
    return dp[-1]
