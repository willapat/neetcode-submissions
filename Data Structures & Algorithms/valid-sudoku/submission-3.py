class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(len(board)): #row
            for j in range(len(board[i])): #col
                if board[i][j] == '.':
                    continue
                index = (i // 3) * 3 + (j // 3)
                print(rows)
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[index]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[index].add(board[i][j]) ####

        return True
