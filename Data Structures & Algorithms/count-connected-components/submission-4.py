class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #undirected edges: [0, 1] 1 --> 0 ... 0 --> 1
        #no loops, everything must descend
        uf = UnionFind(n)
        
        for a, b in edges:
            while uf.parent[a] != a:
                a = uf.parent[a]
            while uf.parent[b] != b:
                b = uf.parent[b]
            if a != b:
                if uf.rank[b] >= uf.rank[a]:
                    larger = b
                    smaller = a
                else:
                    larger = a
                    smaller = b
                
                uf.rank[larger] += uf.rank[smaller]
                uf.parent[smaller] = larger
                uf.count -= 1
        
        return uf.count
        
        
