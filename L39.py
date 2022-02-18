# [Combination Sum] https://leetcode.com/problems/combination-sum/

def combinationSum(candidates, target):
    def dfs(path, need, candi):
        if need == 0:
            ans.append(path)
        elif need > 0:
            for i in range(len(candi)):
                dfs(path+[candi[i]], need-candi[i], candi[i:])
    ans = []
    dfs([], target, candidates)
    return ans
