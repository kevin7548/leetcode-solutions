class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1

        while up <= down:
            row = (up + down) // 2
            if up == down:
                break

            if matrix[row+1][0] <= target:
                up = row + 1
            elif target < matrix[row][0]:
                down = row -1
            else:
                break

        left = 0
        right = len(matrix[row]) - 1
        
        while left <= right:
            column = (left + right) // 2
            if matrix[row][column] < target:
                left = column + 1
            elif target < matrix[row][column]:
                right = column - 1
            else:
                return True
        
        return False