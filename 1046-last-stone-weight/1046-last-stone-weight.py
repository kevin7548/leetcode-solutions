import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)   # -2, -7, -4, -1, -8, -1
        while len(h) > 1:
            x = heapq.heappop(h)    # -8
            y = heapq.heappop(h)    # -7
            heapq.heappush(h, x-y)
        return -heapq.heappop(h)