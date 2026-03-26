class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        # 3,1이면 1을 살려야하기에 right=mid, left<right
        while left < right:
            mid = (left + right) // 2
            # 조건 그냥 하나로
            if nums[mid] > nums[right]:
                left = mid + 1
            else:   # nums[mid] <= nums[right]
                right = mid

        return nums[left]