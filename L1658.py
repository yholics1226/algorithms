# [Minimum Operations to Reduce X to Zero] https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

def minOperations(nums, x):
    n = len(nums)
    y = sum(nums) - x
    s = cnt = 0
    flag = False
    lt = 0
    for rt in range(n):
        s += nums[rt]
        while s > y and lt <= rt:
            s -= nums[lt]
            lt += 1
        if s == y:
            flag = True
            cnt = max(cnt, rt - lt + 1)
    return n - cnt if flag else -1
