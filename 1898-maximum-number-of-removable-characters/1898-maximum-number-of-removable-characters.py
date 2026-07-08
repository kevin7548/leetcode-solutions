class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def sub_check(k):
            j = 0   # p-index
            removed = set(removable[:k])
            for i in range(len(s)):
                if i in removed:
                    continue
                if j < len(p) and s[i] == p[j]: # j의 범위!!
                    j += 1
            return j == len(p)
        
        left, right = 0, len(removable) # left(yes), right(no)
        while left < right:
            mid = (left + right + 1) // 2
            if sub_check(mid):
                left = mid
            else:
                right = mid - 1
        return left