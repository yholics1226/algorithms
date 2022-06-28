# [Minimum Deletions to Make Character Frequencies Unique] https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

from collections import Counter
def minDeletions(s):
    sH = Counter(s)
    cnt = sorted(sH.values(), reverse=True)
    ans, prev = 0, cnt[0] + 1
    for c in cnt:
        if c >= prev:
            ans += c - prev + 1
            if prev > 1:
                prev -= 1
        else:
            prev = c
    return ans

# another solution
from collections import Counter
def minDeletions(s):
    sH = Counter(s)
    cnt = sorted(sH.values(), reverse=True)
    ans = 0
    seen = set()
    for c in cnt:
        if c in seen:
            while c in seen:
                ans += 1
                c -= 1
        if c:
            seen.add(c)
    return ans
