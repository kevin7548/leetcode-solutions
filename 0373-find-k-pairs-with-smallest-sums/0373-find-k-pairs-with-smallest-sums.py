import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        h = []  # (sum, i, j)
        answer = []
        i, j = 0, 0

        # heap에는 min(nums1, k)개의 nums2 첫 원소와의 조합만
        for i in range(min(len(nums1), k)):
            heapq.heappush(h, (nums1[i] + nums2[0] ,i, 0))

        # k개 heappop
        for _ in range(k):
            total, i, j = heapq.heappop(h)
            answer.append((nums1[i], nums2[j]))
            if j < len(nums2)-1:
                heapq.heappush(h, (nums1[i] + nums2[j+1], i, j+1))

        return answer