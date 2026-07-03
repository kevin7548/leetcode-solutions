class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf')
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:    # 중복인 경우 스킵
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_3 = nums[i] + nums[left] + nums[right]
                if sum_3 == target: # 일치하는 경우 조기 종료
                    return sum_3
                if abs(target - sum_3) < abs(target - result):
                    result = sum_3
                if target < sum_3:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:  # 중복
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:    # 중복
                        left += 1
        return result
                
        -4,-1,2
        -4,1,2
        -1,1,2
