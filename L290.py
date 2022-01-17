# [Word Pattern] https://leetcode.com/problems/word-pattern/

def wordPattern(pattern, s):
    s = s.split()
    if len(pattern) != len(s):
        return False
    p2s = dict()
    seen = set()
    for i in range(len(s)):
        if pattern[i] in p2s:
            if p2s[pattern[i]] != s[i]:
                return False
        else:
            if s[i] in seen:
                return False
            else:
                p2s[pattern[i]] = s[i]
                seen.add(s[i])
    return True
