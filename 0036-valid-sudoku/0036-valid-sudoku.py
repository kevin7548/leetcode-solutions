from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row, column, box => 중복 체크
        rows = defaultdict(set)     # 9
        columns = defaultdict(set)  # 9
        boxes = defaultdict(set)    # (3,3) tuple

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.': continue

                if num in rows[i]:
                    return False
                if num in columns[j]:
                    return False
                if num in boxes[(i//3, j//3)]:
                    return False

                rows[i].add(num)
                columns[j].add(num)
                boxes[(i//3, j//3)].add(num)
    
        return True
        
        

    