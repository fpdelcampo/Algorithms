class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        to = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if not stack or to[char] != stack[-1]:
                    return False
                stack.pop()
        if stack:
            return False
        else:
            return True