class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(1, n + 1)]
        self.rank = [1] * n
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #find what edge can be removed to eliminate a loop
        nodesNum = set()
        for a,b in edges:
            nodesNum.add(a)
            nodesNum.add(b)

        uf = UnionFind(len(nodesNum))
        removed = None

        for a,b in edges:
            edgeA = a
            edgeB = b
            while a != uf.parent[a - 1]:
                a = uf.parent[a - 1]
            while b != uf.parent[b - 1]:
                b = uf.parent[b - 1]

            if a != b:
                if uf.rank[b - 1] >= uf.rank[a - 1]:
                    larger = b
                    smaller = a
                else:
                    larger = a
                    smaller = b

                uf.parent[smaller - 1] = larger
                uf.rank[larger - 1] += uf.rank[smaller - 1]
            else:
                removed = [edgeA, edgeB]
        
        return removed