# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None
        count = k

        def traverse(root):
            nonlocal result, count
            if not root:
                return
            
            traverse(root.left)
            count -= 1
            if count == 0:
                result = root.val
            traverse(root.right)
        
        traverse(root)
        return result