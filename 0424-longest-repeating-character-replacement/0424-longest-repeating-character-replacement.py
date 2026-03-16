class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        max_count = 0
        counts = {}

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            # 매번 max 계산하지 말고, max_count만 비교
            max_count = max(max_count, counts[s[right]])
            if right - left + 1 - max_count > k:    # 어차피 한 번만
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len