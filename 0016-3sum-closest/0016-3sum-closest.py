class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf')
        for i in range(len(nums)-2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_3 = nums[i] + nums[left] + nums[right]
                if abs(target - sum_3) < abs(target - result):
                    result = sum_3
                if target < sum_3:
                    right -= 1
                else:
                    left += 1
        return result
                
        -4,-1,2
        -4,1,2
        -1,1,2
