class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for row, col in directions:
                nr, nc = r + row, c + col
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    result += 1

        return result