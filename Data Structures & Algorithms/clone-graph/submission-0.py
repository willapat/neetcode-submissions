"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        #return the neihbors
        old = {} #maps old node to new updated node

        def dfs(node):
            if node in old:
                return old[node]
            
            copy = Node(node.val) #copy old value
            old[node] = copy

            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
    
            return copy
        
        return dfs(node)

        