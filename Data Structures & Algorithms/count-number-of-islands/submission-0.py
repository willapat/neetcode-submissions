class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #islands are groups of 1s that are connected vertical or horizontal (Not diagonal)
        count = 0
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])


        def dfs(r, c):
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for x, y in directions:
                ny, nx = y + r, x + c
                if 0 <= ny < rows and 0 <= nx < cols:
                    dfs(ny, nx)


        for row in range(0, rows):
            for col in range(0, cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1

        return count



         