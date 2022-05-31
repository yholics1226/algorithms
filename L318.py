# [Maximum Product of Word Lengths] https://leetcode.com/problems/maximum-product-of-word-lengths/

def maxProduct(words):
    def isUnique(s1, s2):
        for x in s1:
            if x in s2:
                return False
        return True
    n = len(words)
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if isUnique(words[i], words[j]):
                ans = max(ans, len(words[i]) * len(words[j]))
    return ans

# using set operation
def maxProduct(words):
    n = len(words)
    s = [set(word) for word in words]
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if not (s[i] & s[j]):
                ans = max(ans, len(words[i]) * len(words[j]))
    return ans

# using bit mask (faster)
def maxProduct(words):
    n = len(words)
    mask = [0] * n
    for i in range(n):
        for c in set(words[i]):
            mask[i] |= (1 << (ord(c) - 97))
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if not mask[i] & mask[j]:
                ans = max(ans, len(words[i]) * len(words[j]))
    return ans

# faster solution using bit mask
def maxProduct(words):
    d = {0: 0}
    for word in words:
        mask = 0
        for c in set(word):
            mask |= (1 << (ord(c) - 97))
        d[mask] = max(d.get(mask, 0), len(word))
    return max([d[x] * d[y] for x in d for y in d if not x & y])
