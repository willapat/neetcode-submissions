class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.res = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        def dfs(r, c):
            
            visited.add((r, c))
            for row, col in directions:
                nr, nc = row + r, col + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    if (r, c) not in visited:
                        dfs(nr, nc)
                else:
                    self.res += 1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)

        return self.res