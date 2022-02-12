# [Permutation in String] https://leetcode.com/problems/permutation-in-string/

from collections import Counter
def checkInclusion(s1, s2):
    sH = Counter(s1)
    n = len(s1)
    tmp = Counter(s2[:n])
    if sH == tmp:
        return True
    for i in range(n, len(s2)):
        tmp[s2[i]] += 1
        lt = s2[i-n]
        tmp[lt] -= 1
        if tmp[lt] == 0:
            del tmp[lt]
        if sH == tmp:
            return True
    return False
