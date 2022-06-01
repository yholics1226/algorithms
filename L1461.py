# [Check If a String Contains All Binary Codes of Size K] https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

def hasAllCodes(s, k):
    seen = set()
    for i in range(k, len(s)+1):
        seen.add(s[i-k:i])
    return len(seen) == (1 << k)

# faster
def hasAllCodes(s, k):
    seen = set()
    n = 1 << k
    for i in range(k, len(s)+1):
        code = s[i-k:i]
        if code not in seen:
            seen.add(code)
            n -= 1
            if n == 0:
                return True
    return False
