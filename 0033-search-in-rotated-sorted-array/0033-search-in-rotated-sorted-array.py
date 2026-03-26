class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # mid가 target
            if nums[mid] == target:
                return mid

            # 왼쪽 정렬 여부
            if nums[mid] >= nums[left]:
                if nums[mid] >= target >= nums[left]:
                    right = mid - 1  
                else: 
                    left = mid + 1
            # 오른쪽 정렬
            else: # 5, 1, 2, 3, 4
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1