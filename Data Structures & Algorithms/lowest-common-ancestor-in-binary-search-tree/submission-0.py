# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root, p, q):
        if root.val > p.val and root.val > q.val:
            return self.traverse(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.traverse(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.traverse(root, p, q)
