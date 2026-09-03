class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rows = len(grid)
        cols = len(grid[0])
        
        def bfs():
            queue = deque()
            for row in range(0, rows):
                for col in range(0, cols):
                    if grid[row][col] == 0:
                        queue.append((row, col, 0))
            while queue:
                x, y, z = queue.popleft()

                for r, c in directions:
                    newR, newC = x + r, y + c
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] != -1:
                        if z + 1 < grid[newR][newC]:
                            grid[newR][newC] = z + 1
                            queue.append((newR, newC, z + 1))
        

        bfs()






