class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # row check
        allowed = set("123456789.")
        for row in board:
            # check the digits and .
            row_set = set(row)
            if not row_set.issubset(allowed):
                return False
            # check duplicates
            row_counts = Counter(row)
            for item, count in row_counts.items():
                if count > 1 and item != '.':
                    return False
            
        # col check
        transposed_board = [list(col) for col in zip(*board)]
        for col in transposed_board:
            # check duplicates
            col_counts = Counter(col)
            for item, count in col_counts.items():
                if count > 1 and item != ".":
                    return False 

        # 3x3 matrix check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        cell = board[row][col]

                        if cell == '.':
                            continue
                        if cell in seen:
                            return False
                        
                        seen.add(cell)
        return True
