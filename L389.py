# [Find the Difference] https://leetcode.com/problems/find-the-difference/

from collections import Counter
def findTheDifference(s, t):
    sH = Counter(s)
    tH = Counter(t)
    for x in tH:
        if tH[x] != sH[x]:
            return x
