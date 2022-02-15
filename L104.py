# [Maximum Depth of Binary Tree] https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lt = self.maxDepth(root.left)
        rt = self.maxDepth(root.right)
        return max(lt, rt) + 1

# another solution (BFS)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        Q = deque([root])
        d = 0
        while Q:
            n = len(Q)
            for i in range(n):
                x = Q.popleft()
                if x.left:
                    Q.append(x.left)
                if x.right:
                    Q.append(x.right)
            d += 1
        return d
