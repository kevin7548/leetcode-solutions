class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(C):
            w, d = 0, 1
            for weight in weights:
                w += weight
                if w > C:
                    d += 1
                    w = weight
            return d <= days
        
        lo, hi = max(weights), sum(weights) # lo(F), hi(T)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_ship(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
        