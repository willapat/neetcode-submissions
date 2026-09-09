class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #so from any node, if you drop water on that node can it spill into both oceans
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()
        pacific_starts = []
        atlantic_starts = []

        res = []

        def dfs(r, c, ocean):
            for row, col in directions:
                nr, nc = r + row, c + col
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in ocean and heights[nr][nc] >= heights[r][c]:
                    ocean.add((nr, nc))
                    dfs(nr, nc, ocean)

            return

                
    
        for row in range(0, rows):
            for col in range(0, cols):
                if row == 0 or col == 0:
                    pacific.add((row, col))
                    pacific_starts.append((row, col))
                if row == rows - 1 or col == cols - 1:
                    atlantic.add((row, col))
                    atlantic_starts.append((row, col))



        for r, c in pacific_starts:
            dfs(r, c, pacific)
        for r, c in atlantic_starts:
            dfs(r, c, atlantic)

        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r, c])
        
        return res
        


        
