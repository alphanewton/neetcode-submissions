class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                target = board[r][c]
                if target == ".":
                    continue
                if target in rows[r] or target in cols[c] or target in squares[(r//3,c//3)]:
                    return False
                cols[c].add(target)
                rows[r].add(target)
                squares[(r//3, c//3)].add(target)
        
        return True