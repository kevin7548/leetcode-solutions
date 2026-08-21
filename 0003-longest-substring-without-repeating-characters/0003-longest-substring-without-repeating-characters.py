class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}   # {char: 마지막 idx}
        max_len, left = 0, 0

        for right in range(len(s)):
            ch = s[right]
            if ch in last:
                left = max(left, last[ch] + 1)
            last[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len