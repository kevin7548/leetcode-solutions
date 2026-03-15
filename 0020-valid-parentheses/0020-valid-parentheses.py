class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if stack and stack.pop() + char in ['()', '{}', '[]']:
                    continue
                
                # last = stack.pop()
                # if last + char in :
                #     continue
                else:
                    return False

        if not stack:
            return True
        else:
            return False
