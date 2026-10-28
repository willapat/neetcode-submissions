# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        if not root:
            return res
        q.append(root)
        while q:
            length = len(q)
            level = []
            for i in range(length):
                removed = q.popleft()
                level.append(removed.val)
                if removed.left:
                    q.append(removed.left)
                if removed.right:
                    q.append(removed.right)
            res.append(level)
        
        return res