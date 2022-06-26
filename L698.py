# [Partition to K Equal Sum Subsets] https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

def canPartitionKSubsets(nums, k):
    nums.sort(reverse=True)
    s = sum(nums) // k
    partition = [0] * k
    def dfs(idx):
        if idx == len(nums):
            return len(set(partition)) == 1
        for i in range(k):
            partition[i] += nums[idx]
            if partition[i] <= s and dfs(idx + 1):
                return True
            partition[i] -= nums[idx]
            if partition[i] == 0:
                break
        return False
    return dfs(0)
