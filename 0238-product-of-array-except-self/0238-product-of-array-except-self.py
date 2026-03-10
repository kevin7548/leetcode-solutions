class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # i번째 기준, 0~i-1은 prefix, i+1~n-1은 suffix
        n = len(nums)
        array = [0 for _ in range(n)]
        prefix = [nums[0]] * n
        suffix = [nums[-1]] * n

        for i in range(n-1):  # 0 ~ n-2
            prefix[i+1] = prefix[i] * nums[i+1]
            suffix[n-2-i] = suffix[n-1-i] * nums[n-2-i]
        
        array[0] = suffix[1]
        array[n-1] = prefix[n-2]
        for i in range(1, n-1): # 1 ~ n-2
            array[i] = prefix[i-1] * suffix[i+1]

        return array
        