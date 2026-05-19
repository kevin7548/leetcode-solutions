class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # 왼쪽 정렬
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:   # 오른쪽 정렬
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    # [4, 5, 6, 7, 0, 1, 2] target=0 => 4<7, (7<2)
    #                     target 5 => (4<7), 7<2
    # [6, 7, 0, 1, 2, 4, 5] target=0 => (6<1), 1<5
    #                     target 4 => 6<1, (1<5)