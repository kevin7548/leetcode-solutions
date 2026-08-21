from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, left = 0, 0

        for right in range(len(s)):
            # 현재 substring에 있는지 확인
            ch, S = s[right], s[left:right]
            if ch in S:
                # ch=a right=4
                left = left + S.index(ch) + 1 # 2
            max_len = max(max_len, right - left + 1)

        return max_len

        # 해시 안 쓴 이유: left 당길 때 삭제하기 너무 번거롭다