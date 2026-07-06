class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def sub_check(k):
            j = 0
            removed = set(removable[:k])    # {1,3}
            for i in range(len(s)): # 0~5
                if i in removed:
                    continue
                if j < len(p) and s[i] == p[j]: # p 다 확인해도 for문 돈다
                    j += 1
            return j == len(p)

        left, right = 0, len(removable)
        while left < right:
            mid = (left + right + 1) // 2   # 0(yes), 1(no), 5(no)
            if sub_check(mid):
                left = mid
            else:
                right = mid - 1
        return left
