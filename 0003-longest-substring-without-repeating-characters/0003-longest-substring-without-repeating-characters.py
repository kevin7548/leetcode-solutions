class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        substr = ""
        max_len = 0 # s = ""인 edge case

        for right in range(len(s)): # 0~7
            if s[right] not in substr:
                substr += s[right]
                max_len = max(max_len, len(substr))
            else:
                left += substr.index(s[right]) + 1
                substr = s[left:right+1]
        
        return max_len
        
        # right 다음 탐색
        # 1. 새로운 거 => substring에 포함, right += 1
        # 2. 있던 거 => 그 전 substring => max_len, substring left전진, left, right 모두 중복 있는 지점으로 

        return max_length