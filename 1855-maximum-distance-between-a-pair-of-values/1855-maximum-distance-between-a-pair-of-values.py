class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_dist = 0
        i = 0

        for j in range(len(nums2)):
            # while 문에 i 이동, 무한루프 방지
            while i <= j and i < len(nums1) and nums1[i] > nums2[j]:
                i += 1
            if i <= j and i < len(nums1) and nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
        
        return max_dist
