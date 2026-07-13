# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.encoded = ""
        def helper(node):
            if len(self.encoded) == 0:
                comma = ""
            else:
                comma = ","

            if not node:
                self.encoded += comma + "N"
                return None
            else:
                self.encoded += comma + str(node.val)

            helper(node.left)
            helper(node.right)
        
        helper(root)
        print(self.encoded)
        return self.encoded
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0

        def helper():
            if values[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = helper()
            node.right = helper()
            return node

        return helper()