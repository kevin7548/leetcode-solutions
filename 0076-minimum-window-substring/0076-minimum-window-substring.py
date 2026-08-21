from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = defaultdict(int)   # {문자열: 개수}
        left = 0
        num, total = 0, len(t_count)   # 만족하는 문자 개수
        min_len, min_sub = float('inf'), ""

        for right in range(len(s)):
            char = s[right]
            s_count[char] += 1
            if char in t_count and s_count[char] == t_count[char]:
                num += 1
            while num == total:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_sub = s[left:right+1]
                left_char = s[left]
                if left_char in t_count:
                    s_count[left_char] -= 1
                    if s_count[left_char] < t_count[left_char]:
                        num -= 1
                left += 1
        
        return min_sub
                