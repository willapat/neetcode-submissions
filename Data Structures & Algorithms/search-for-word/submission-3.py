class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #len of path is index of word you want to find

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, i):
            if i == len(word) - 1:
                return True
            
            visited.add((r, c))
            for row, col in directions:
                nr, nc = r + row, c + col
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == word[i + 1] and (nr, nc) not in visited:
                    if backtrack(nr, nc, i + 1):
                        return True
            visited.remove((r, c))
            
            return False

        start = word[0]
        lis = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == start:
                    lis.append((r, c))

        for row, col in lis:
            if backtrack(row, col, 0):
                return True
        return False