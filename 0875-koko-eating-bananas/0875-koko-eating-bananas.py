import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(K):
            hour = 0
            for p in piles:
                hour += math.ceil(p / K)
            return hour <= h
        
        lo, hi = 1, max(piles)
        while lo < hi:  # lo(no), hi(yes)
            mid = (lo + hi) // 2
            if can_eat(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

