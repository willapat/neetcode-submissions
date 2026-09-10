class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #None of 0's on edge of board
        #Problem: Any group of 0's that cannot reach the edge, turn to X
        #rather than checking every spot, why dont we check every spot but the outside row/col
        #check if its a 0, then dfs on neighbors if 0
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != "O":
                return
            board[r][c] = "S"          # safe
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                board[r][c] = "O" if board[r][c] == "S" else "X"

            