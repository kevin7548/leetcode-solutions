class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        max_dist = 0

        for j in range(len(nums2)):
            # 1. i 전진
            while i < len(nums1) and i < j and nums1[i] > nums2[j]:
                i += 1
            # 2. max_dist 측정
            if i < len(nums1) and i <= j and nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j-i)

        return max_dist

        # [2,2,2] [10,10,1]
        2,10 