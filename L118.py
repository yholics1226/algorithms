# [Pascal's Triangle] https://leetcode.com/problems/pascals-triangle/

def generate(numRows):
    ans = [[1]]
    for _ in range(numRows-1):
        pre = ans[-1]
        tmp = [1]
        for i in range(len(pre)-1):
            tmp.append(pre[i] + pre[i+1])
        tmp.append(1)
        ans.append(tmp)
    return ans
