class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        s = set(nums)    # []: 길이

        for num in s:
            if num - 1 in s:
                continue
            length = 1
            cur = num
            while cur + 1 in s:
                length += 1
                cur += 1
            max_len = max(length, max_len)

        return max_len