from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have, need_count = 0, len(need)
        window = defaultdict(int)
        result = ""
        min_len = float('inf')
        left = 0

        for right in range(len(s)):
            char = s[right]
            # window, have
            window[char] += 1
            if char in need and window[char] == need[char]:
                have += 1
        
            while have == need_count:
                # result
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]
                # left 이동
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return result