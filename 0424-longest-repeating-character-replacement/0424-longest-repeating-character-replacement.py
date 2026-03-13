class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        counts = {}

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            length, max_count = sum(counts.values()), max(counts.values())
            
            while length - max_count > k:
                counts[s[left]] = counts.get(s[left]) - 1
                left += 1
                length -= 1

            max_len = max(max_len, length)

        return max_len