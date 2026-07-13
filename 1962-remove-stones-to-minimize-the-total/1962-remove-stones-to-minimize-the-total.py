import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = [-p for p in piles]
        heapq.heapify(h)
        count = 0

        while count < k:
            m = -heapq.heappop(h)    # 9
            n = m - floor(m/2)  # 5
            heapq.heappush(h, -n)
            count += 1
        
        return -sum(h)    # h: [-5, -4, -3]