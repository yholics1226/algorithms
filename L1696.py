# [Jump Game VI] https://leetcode.com/problems/jump-game-vi/

from collections import deque
def maxResult(nums, k):
    q = deque([(nums[0], 0)])
    for i in range(1, len(nums)):
        while q and i > q[0][1] + k:
            q.popleft()
        score = nums[i] + q[0][0]
        while q and score >= q[-1][0]:
            q.pop()
        q.append((score, i))
    return q[-1][0]
