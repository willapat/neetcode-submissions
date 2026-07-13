# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #there are negative values
        #any connecting nodes can form a path

        self.mSum = float('-inf')
        def helper(node):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)
                
            left = max(left, 0)
            right = max(right, 0)

            self.mSum = max(self.mSum, node.val + left + right)

            return node.val + max(left, right)
            
        
        helper(root)
        return self.mSum
        
