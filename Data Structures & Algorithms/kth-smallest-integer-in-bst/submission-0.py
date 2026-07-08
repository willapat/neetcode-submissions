# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #k = 1, the smallest val
        #this is like in order traversal
        self.arr = []

        def helper(node):
            if not node:
                return None
            helper(node.left)
            self.arr.append(node.val)
            helper(node.right)
        helper(root)
        return self.arr[k - 1]