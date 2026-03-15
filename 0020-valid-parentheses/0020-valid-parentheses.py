class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pairs: # 닫는 기호
                last = stack.pop() if stack else '#'
                if pairs[char] == last:
                    continue
                else:
                    return False
            else: # 여는 기호
                stack.append(char)

        return not stack
