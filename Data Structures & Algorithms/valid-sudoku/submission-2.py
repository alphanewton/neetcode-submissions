class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            colSet = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in colSet:
                    return False
                colSet.add(board[r][c])
        
        for c in range(9):
            rowSet = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowSet:
                    return False
                rowSet.add(board[r][c])

        sectionMap = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in sectionMap[(r//3, c//3)]:
                    return False
                sectionMap[(r//3, c//3)].add(board[r][c])
        

        return True

            
            