import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)   # for문으로 하나씩 넣기보다 heapify 활용
        while len(h) > 1:
            x = heapq.heappop(h)
            y = heapq.heappop(h)  
            if x != y:
                heapq.heappush(h, x-y) # x <= y
        return -h[0] if h else 0     # stone 없는 경우