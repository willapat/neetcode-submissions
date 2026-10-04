# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p != None and q == None:
            return False
        elif p == None and q != None:
            return False
        elif p.val != q.val:
            return False
        
        return self.isSameTree(p.left if p != None else None, q.left if q != None else None) and self.isSameTree(p.right if p != None else None, q.right if q != None else None)
