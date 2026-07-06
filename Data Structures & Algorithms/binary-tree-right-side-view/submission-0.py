# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #so kind of like the level order, but only add the rightmost element in that list?

        q = deque()
        res = []
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level[-1].val)
        return res