class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        filtered = [letter for letter in s.lower() if letter.isalnum()]
        
        return filtered == filtered[::-1]
        
        