class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in pairs:   # 닫는 괄호
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:   # 여는 괄호
                stack.append(char)
        return not stack