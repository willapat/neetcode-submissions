# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.value = True

        def helper(node):
            if node == None:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)

            if left > right + 1 or left + 1 < right:
                self.value = False
            
            return 1 + max(left, right)

        
        helper(root)

        return self.value