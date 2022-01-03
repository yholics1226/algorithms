# [Find the Town Judge] https://leetcode.com/problems/find-the-town-judge/

def findJudge(n, trust):
    odeg = [0 for _ in range(n+1)]
    ideg = [0 for _ in range(n+1)]
    for [x, y] in trust:
        odeg[x] += 1
        ideg[y] += 1
    for i in range(1, n+1):
        if odeg[i] == 0 and ideg[i] == n-1:
            return i
    return -1
