import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            cur_cap, total_d = 0, 1
            for w in weights:
                cur_cap += w
                if cur_cap > capacity:
                    cur_cap = w
                    total_d += 1
            return total_d <= days
        
        left, right = max(weights), sum(weights)    # 10(no) < mid=15(yes) < 55(yes)
        while left < right:
            mid = (left + right) // 2   
            # 32(10,32), 21(10,21), 15(10,15), 12(13,15), 14(15,15)
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left
