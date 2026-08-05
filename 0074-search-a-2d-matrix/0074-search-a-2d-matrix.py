class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n -1

        while left < right:
            mid = (left + right) // 2
            a, b = mid // n, mid % n
            if matrix[a][b] == target:
                return True
            elif matrix[a][b] > target:
                right = mid - 1
            else:
                left = mid + 1

        return target == matrix[left // n][left % n]

        # 0, 11 => 5        0, 11 => 5
        # 0, 4 => 2         0, 5 => 2
        # 0, 1 => 0         0, 2 => 1
        # 1, 1 => 1         