from collections import Counter, defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        count = defaultdict(int)  # {문자: 개수}

        for right in range(len(s)):
            count[s[right]] += 1
            # left 갱신
            while (right-left+1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            # length 갱신
            max_len = max(max_len, right-left+1)

        return max_len