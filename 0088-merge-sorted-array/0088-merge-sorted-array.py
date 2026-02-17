class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # For each of the zeros, modify into elements from nums2
        for i in range(n):
            nums1[m + i] = nums2[i]

            #nums1의 m, m+1, m+2 => 개수 n 개
            #nums2의 0, 1, 2
            
        nums1.sort()

        return nums1