# [Valid Palindrome II] https://leetcode.com/problems/valid-palindrome-ii/

def validPalindrome(s):
    if s == s[::-1]:
        return True
    lt = 0
    rt = len(s) - 1
    while lt < rt:
        if s[lt] == s[rt]:
            lt += 1
            rt -= 1
        else:
            s1 = s[lt:rt]
            s2 = s[lt+1:rt+1]
            if s1 == s1[::-1]:
                return True
            return s2 == s2[::-1]
