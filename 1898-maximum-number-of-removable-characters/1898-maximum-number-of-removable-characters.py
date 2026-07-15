class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def subseq(K):
            removed = set(removable[:K])
            j = 0   # 다음에 매칭할 p의 인덱스
            for i in range(len(s)):
                if i in removed:
                    continue
                if j < len(p) and s[i] == p[j]:
                    j += 1
            return j == len(p) # 그래야 p 모두 매칭완료.
        
        lo, hi = 0, len(removable)
        while lo < hi:  # lo(yes), hi(no)
            mid = (lo + hi + 1) // 2
            if subseq(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo