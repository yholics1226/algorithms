# [Maximum Width of Binary Tree] https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        Q = deque([(1, root)])
        while Q:
            s = Q[0][0]
            n = len(Q)
            for _ in range(n):
                i, x = Q.popleft()
                if x.left:
                    Q.append((i*2, x.left))
                if x.right:
                    Q.append((i*2+1, x.right))
            ans = max(ans, i - s + 1)
        return ans
