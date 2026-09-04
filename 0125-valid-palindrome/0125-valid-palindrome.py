class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. 소문자화 s = s.lower()
        # 2. remove all non-alphanumeric char 
        # for문으로 .isalnum() 확인 후 추가
        # return s == s[::-1]

        s = s.lower()
        string = ""
        for char in s:
            if char.isalnum():
                string += char
            else:
                continue

        return string == string[::-1]