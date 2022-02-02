# [Find All Anagrams in a String] https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import defaultdict
def findAnagrams(s, p):
    answer = []
    sH = defaultdict(int)
    pH = defaultdict(int)
    n = len(p)
    for x in p:
        pH[x] += 1
    for x in s[:n]:
        sH[x] += 1
    if sH == pH:
        answer.append(0)
    lt = 0
    while lt < len(s) - n:
        sH[s[lt]] -= 1
        if sH[s[lt]] == 0:
            del sH[s[lt]]
        sH[s[lt+n]] += 1
        if sH == pH:
            answer.append(lt+1)
        lt += 1
    return answer
