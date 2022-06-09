# [Remove Palindromic Subsequences] https://leetcode.com/problems/remove-palindromic-subsequences/

def removePalindromeSub(s):
    return 1 if s == s[::-1] else 2

# using two pointers
def removePalindromeSub(s):
    lt, rt = 0, len(s) - 1
    while lt < rt:
        if s[lt] != s[rt]:
            return 2
        lt += 1
        rt -= 1
    return 1
