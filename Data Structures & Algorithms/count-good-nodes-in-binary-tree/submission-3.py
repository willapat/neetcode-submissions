# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #if all prev nodes are lesser value, then it is a good node
        self.count = 1

        def traverse(node, high):
            if not node:
                return None
            if node.left and high <= node.left.val:
                self.count += 1
                traverse(node.left, node.left.val)
            else:
                traverse(node.left, high)
            if node.right and high <= node.right.val:
                self.count += 1
                traverse(node.right, node.right.val)
            else:
                traverse(node.right, high)

        traverse(root, root.val)
        return self.count
