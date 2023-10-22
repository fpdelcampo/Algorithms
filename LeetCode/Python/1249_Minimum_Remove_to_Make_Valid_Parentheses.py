class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        rm = []
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    rm.append(idx)
        stack = set(stack)
        rm = set(rm)
        res = ""
        for idx, char in enumerate(s):
            if idx not in rm and idx not in stack:
                res += char
            idx += 1
        return res