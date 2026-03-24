class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 조건 많이 달수록 edge case 실수 (ex) if up == down, row + 1
        # 2차원으로 row, column 두 번 검색하지 않고, 1차원으로 해석
        M, N = len(matrix), len(matrix[0])
        left = 0
        right = M * N - 1
        
        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // N][mid % N]
            if target > value:
                left = mid + 1
            elif target < value:
                right = mid - 1
            else:
                return True
        
        return False