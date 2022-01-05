# [Palindrome Partitioning] https://leetcode.com/problems/palindrome-partitioning/

def partition(s):
    def isPalindrome(lt, rt):
        while lt < rt:
            if s[lt] != s[rt]:
                return 0
            lt += 1
            rt -= 1
        return 1
    n = len(s)
    ans = [[] for _ in range(n+1)]
    ans[0].append([])
    for i in range(n):
        for j in range(i+1):
            if isPalindrome(j, i):
                sub = s[j:i+1]
                for x in ans[j]:
                    ans[i+1].append(x + [sub])
    return ans[-1]
