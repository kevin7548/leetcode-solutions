class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1] * n, [1] * n
        for i in range(n-1):
            prefix[i+1] = prefix[i] * nums[i] # [1, 1, 2, 6]
            suffix[n-2-i] = suffix[n-1-i] * nums[n-1-i] # [24, 12, 4, 1]
        
        answer = [0] * n
        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer
