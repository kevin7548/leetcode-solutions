class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # [-4, -1, -1, 0, 1, 3]
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:    # i에 대한 중복
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:   # total > 0
                    right -= 1
        
        return result
