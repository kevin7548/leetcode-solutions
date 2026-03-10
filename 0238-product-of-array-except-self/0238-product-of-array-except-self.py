class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # i번째 기준, 0~i-1은 prefix, i+1~n-1은 suffix
        n = len(nums)
        array = [1] * n

        # prefix [1, 1, 2, 6]
        prefix = 1
        for i in range(n):
            array[i] = prefix
            prefix *= nums[i]

        # suffix [24, 12, 4, 1]
        suffix = 1
        for j in range(-1, -n-1, -1):
            array[j] *= suffix
            suffix *= nums[j]

        return array
        
        # prefix, suffix 한 정수로 array 하나로 처리