# [트리] https://www.acmicpc.net/problem/4256

# slightly modifying the solution in L105.py (https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
import sys
input = sys.stdin.readline
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def buildTree(preorder, inorder):
    if inorder:
        idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[idx])
        root.left = buildTree(preorder, inorder[:idx])
        root.right = buildTree(preorder, inorder[idx+1:])
        return root
def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.val, end=' ')
t = int(input())
for _ in range(t):
    n = int(input())
    preorder = [*map(int, input().split())]
    inorder = [*map(int, input().split())]
    tree = buildTree(preorder, inorder)
    postorder(tree)
    print()

# another solution (much faster)
import sys
input = sys.stdin.readline
def post(si, ei, sp, ep):
    if si <= ei:
        x = idx[preorder[sp]]
        post(si, x-1, sp+1, sp+x-si)
        post(x+1, ei, x-si+sp+1, ep)
        postorder.append(preorder[sp])
t = int(input())
for _ in range(t):
    n = int(input())
    preorder = [*map(int, input().split())]
    inorder = [*map(int, input().split())]
    idx = [0] * (n+1)
    for i in range(n):
        idx[inorder[i]] = i
    postorder = []
    post(0, n-1, 0, n-1)
    print(*postorder)
