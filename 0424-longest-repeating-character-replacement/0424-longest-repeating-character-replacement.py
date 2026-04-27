from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_len = 0
        max_count = 0
        left = 0

        for right in range(len(s)):
            # 1. 원소 count에 추가
            counts[s[right]] = counts.get(s[right], 0) + 1
            # 2. max_count
            max_count = max(max_count, counts[s[right]])
            # 3. left. 가장 길었던 윈도우를 찾으므로 굳이 while X, 윈도우 길이 유지
            if (right - left + 1) - max_count > k:
                counts[s[left]] -= 1
                left += 1
            # 4. max_len
            max_len = max(max_len, right - left + 1)
        
        return max_len
            
            


            
