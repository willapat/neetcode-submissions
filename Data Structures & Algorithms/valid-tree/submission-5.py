class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #undirected edges: [0, 1] 1 --> 0 ... 0 --> 1
        #no loops, everything must descend
        dic = {}
        for i in range(n):
            dic[i] = []
        for a, b in edges:
            dic[a].append(b) #maps edges to nodes
            dic[b].append(a)

        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for edge in dic[node]:
                if edge != prev and not dfs(edge, node):
                    return False

            return True  
        
        return dfs(0, -1) and len(visited) == n


