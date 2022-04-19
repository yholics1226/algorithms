# [Increasing Order Search Tree] https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        stack = []
        def ino(node):
            if node.left:
                ino(node.left)
            stack.append(node.val)
            if node.right:
                ino(node.right)
        ino(root)
        ans = TreeNode(stack.pop())
        while stack:
            ans = TreeNode(stack.pop(), None, ans)
        return ans
