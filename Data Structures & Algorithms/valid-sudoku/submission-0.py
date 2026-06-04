class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        boxes = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                box_index = (i // 3) * 3 + (j // 3)
                if board[i][j] in rows[i] or board[i][j] in cols[j]:
                    return False
                elif board[i][j] == ".":
                    pass
                elif board[i][j] in boxes[box_index]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[box_index].add(board[i][j])
        return True
        