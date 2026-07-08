# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.count = 0
        self.val = None
        def helper(node):
            if not node:
                return None

            helper(node.left)
            self.count += 1
            if self.count == k:
                self.val = node.val
                return None
            helper(node.right)

        helper(root)
        return self.val