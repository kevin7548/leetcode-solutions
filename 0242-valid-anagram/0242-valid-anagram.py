from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 길이 다른 경우 바로 제외 => 성능 최적화
        if len(s) != len(t):
            return False
        
        s_counts = Counter(s)
        t_counts = Counter(t)
        
        # 바로 비교해서 return
        return s_counts == t_counts