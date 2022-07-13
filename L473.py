# [Matchsticks to Square] https://leetcode.com/problems/matchsticks-to-square/

def makesquare(matchsticks):
    s = sum(matchsticks)
    if s % 4:
        return False
    n, k = len(matchsticks), s // 4
    matchsticks.sort(reverse=True)
    res = [0] *  4
    def dfs(idx):
        if idx == n:
            return True
        for i in range(4):
            res[i] += matchsticks[idx]
            if res[i] <= k and dfs(idx+1):
                return True
            res[i] -= matchsticks[idx]
            if res[i] == 0:
                break
        return False
    return dfs(0)
