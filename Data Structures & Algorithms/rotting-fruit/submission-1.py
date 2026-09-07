class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #run bfs on rotten fruits, maybe do a sweep at first to get count of good
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        
        def bfs():
            queue = deque()
            for row in range(0, rows):
                for col in range(0, cols):
                    if grid[row][col] == 2:
                        queue.append((row, col))
            time = 0
            while queue:
                for _ in range(len(queue)): 
                    r, c = queue.popleft()
                    for R, C in directions:
                        nr, nc = r + R, c + C
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            queue.append((nr, nc))
                            grid[nr][nc] = 2
                if len(queue) == 0:
                    return time
                time += 1
            
            return time

        val = bfs()
        for row in range(0, rows):
            for col in range(0, cols):
                if grid[row][col] == 1:
                    return -1
        return val