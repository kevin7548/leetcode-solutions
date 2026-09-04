class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. 소문자화 s = s.lower()
        # 2. remove all non-alphanumeric char 
        # for문으로 .isalnum() 확인 후 추가
        # return s == s[::-1]

        s = [c.lower() for c in s if c.isalnum()]
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True