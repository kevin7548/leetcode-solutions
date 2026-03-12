class Solution:
    def maxArea(self, height: List[int]) -> int:
        # just in case
        if not height:
            return 0
        
        l, r = 0, len(height)-1
        S_max = 0
        
        # S 계산 한번만. more clean
        while l < r:
            S = min(height[l], height[r]) * (r-l)
            S_max = max(S_max, S)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return S_max