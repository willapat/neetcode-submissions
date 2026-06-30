# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swap(self, node):
        if node == None:
            return None
        l_sub = node.left
        self.swap(l_sub)
        r_sub = node.right
        self.swap(r_sub)
        node.right = l_sub
        node.left = r_sub
        


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #so the left subtree and right subtree need to like swap palces
        self.swap(root)

        return root