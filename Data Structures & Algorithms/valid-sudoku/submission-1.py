class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9): # 9 indicies in the row to check
            for c in range(9): # 9 indicies in the column to check
                if board[r][c] == ".": # checks if the space if empty, empty places are frilled with a dot "."
                    continue # if empty we continue
                if (board[r][c] in rows[r] or # if the same number already exists in that row, then we retun false
                    board[r][c] in columns[c] or # if the number already exists in that columbn then we return false
                    board[r][c] in squares[(r // 3, c // 3)]): # if the number already exists in that square, then we return false
                    return False
                # when we pass all those tests, we add numbers 
                columns[c].add(board[r][c]) # adds the new number to the column
                rows[r].add(board[r][c]) # add the new number to the row
                squares[(r // 3, c // 3)].add(board[r][c]) # add the new number to the square
        return True # return True after
