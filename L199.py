# [Binary Tree Right Side View] https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque([(root, 0)])
        d = -1
        while q:
            node, depth = q.popleft()
            if node.right:
                q.append((node.right, depth+1))
            if node.left:
                q.append((node.left, depth+1))
            if depth > d:
                ans.append(node.val)
                d = depth
        return ans
