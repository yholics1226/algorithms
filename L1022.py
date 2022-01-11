# [Sum of Root To Leaf Binary Numbers] https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(ps, tn):
            if tn.left == None and tn.right == None:
                self.ans += ps * 2 + tn.val
            else:
                if tn.left:
                    dfs(ps * 2 + tn.val, tn.left)
                if tn.right:
                    dfs(ps * 2 + tn.val, tn.right)
        dfs(0, root)
        return self.ans
