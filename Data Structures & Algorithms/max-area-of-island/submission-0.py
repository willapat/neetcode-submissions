class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        directions = [(0,1), (0, -1) , (1,0), (-1,0)]

        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            count = 0
            if grid[row][col] == 0:
                return 0
            visited.add((row, col))
            count += 1
            for r, c in directions:
                nr, nc = row + r, col + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    count += dfs(nr, nc)
            return count

        for row in range(0, rows):
            for col in range(0, cols):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    if area > maxArea:
                        maxArea = area
        
        return maxArea