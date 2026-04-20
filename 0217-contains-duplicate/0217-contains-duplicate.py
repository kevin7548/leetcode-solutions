class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums, set(nums) 비교
        return len(nums) != len(set(nums))